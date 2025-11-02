import json
from datetime import datetime, timedelta, timezone
from problem.api.app import app, Base, engine

def setup_function():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def post(c, body, k="k1"):
    return c.post("/v1/appointments",
                  data=json.dumps(body),
                  headers={"Content-Type":"application/json","Idempotency-Key":k})

def test_create_list_sorted():
    c = app.test_client()
    s1 = datetime(2025,3,10,16,0,tzinfo=timezone.utc)
    s2 = datetime(2025,3,10,17,0,tzinfo=timezone.utc)
    for t in (s2, s1):
        r = post(c, {"caregiverId":"c1","patientId":"p1","start":t.isoformat(),"end":(t+timedelta(minutes=30)).isoformat()}, k=t.isoformat())
        assert r.status_code == 201
    r = c.get("/v1/appointments?caregiverId=c1")
    data = r.get_json()
    assert [i["start"] for i in data["items"]] == [s1.isoformat(), s2.isoformat()]

def test_overlap_rejected():
    c = app.test_client()
    s = datetime(2025,3,10,16,0,tzinfo=timezone.utc)
    e = s + timedelta(minutes=30)
    assert post(c, {"caregiverId":"c1","patientId":"p1","start":s.isoformat(),"end":e.isoformat()}).status_code == 201
    r = post(c, {"caregiverId":"c1","patientId":"p2","start":(s+timedelta(minutes=15)).isoformat(),"end":(s+timedelta(minutes=45)).isoformat()}, k="k2")
    assert r.status_code == 409
    assert r.get_json()["code"] == "APPT_OVERLAP"

def test_business_hours():
    c = app.test_client()
    # 07:50 PT on 2025-03-10 is 14:50 UTC
    s = datetime(2025,3,10,14,50,tzinfo=timezone.utc)
    r = post(c, {"caregiverId":"c1","patientId":"p1","start":s.isoformat(),"end":(s+timedelta(minutes=20)).isoformat()}, k="k3")
    assert r.status_code == 422
    assert r.get_json()["code"] == "OUT_OF_BUSINESS_HOURS"

def test_idempotency():
    c = app.test_client()
    s = datetime(2025,3,10,16,0,tzinfo=timezone.utc)
    body = {"caregiverId":"c1","patientId":"p1","start":s.isoformat(),"end":(s+timedelta(minutes=30)).isoformat(),"notes":"n"}
    assert post(c, body, k="same").status_code == 201
    r = post(c, body, k="same")
    assert r.status_code == 201

def test_idempotency_mismatch():
    c = app.test_client()
    s = datetime(2025,3,10,16,0,tzinfo=timezone.utc)
    assert post(c, {"caregiverId":"c1","patientId":"p1","start":s.isoformat(),"end":(s+timedelta(minutes=30)).isoformat()}, k="mix").status_code == 201
    r = post(c, {"caregiverId":"c1","patientId":"DIFF","start":s.isoformat(),"end":(s+timedelta(minutes=30)).isoformat()}, k="mix")
    assert r.status_code == 409
