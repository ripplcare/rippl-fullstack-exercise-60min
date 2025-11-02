from datetime import datetime
from dateutil import tz, parser
from flask import Flask, jsonify, request

from .db import Base, engine, SessionLocal
from .models import Appointment  # noqa: F401

app = Flask(__name__)
Base.metadata.create_all(engine)

PT = tz.gettz("America/Los_Angeles")

def err(code, msg, http=400):
  return jsonify({"code": code, "message": msg}), http

def parse_utc(s: str) -> datetime:
  dt = parser.isoparse(s)
  if not dt.tzinfo:
    raise ValueError("timestamp must be timezone-aware")
  return dt.astimezone(tz.UTC)

def to_utc_iso(dt: datetime) -> str:
  if dt.tzinfo is None:
    dt = dt.replace(tzinfo=tz.UTC)
  return dt.astimezone(tz.UTC).isoformat()

def within_business_hours(start_utc: datetime, end_utc: datetime) -> bool:
  s = start_utc.astimezone(PT)
  e = end_utc.astimezone(PT)
  return (s.hour > 8 or (s.hour == 8 and s.minute >= 0)) and \
         (e.hour < 18 or (e.hour == 18 and e.minute == 0))

@app.post("/v1/appointments")
def create_appointment():
  # TODO: implement POST to satisfy tests in problem/api/tests/test_api.py
  return err("NOT_IMPLEMENTED", "Implement POST /v1/appointments", 501)

@app.get("/v1/appointments")
def list_appointments():
  # TODO: implement GET to satisfy tests in problem/api/tests/test_api.py
  return err("NOT_IMPLEMENTED", "Implement GET /v1/appointments", 501)
