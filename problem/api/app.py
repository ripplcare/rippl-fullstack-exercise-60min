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
    """Parse ISO8601 string and normalize to UTC."""
    dt = parser.isoparse(s)
    if not dt.tzinfo:
        raise ValueError("timestamp must be timezone-aware")
    return dt.astimezone(tz.UTC)

def to_utc_iso(dt: datetime) -> str:
    """Serialize datetimes with an explicit +00:00 offset."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz.UTC)
    return dt.astimezone(tz.UTC).isoformat()

def within_business_hours(start_utc: datetime, end_utc: datetime) -> bool:
    """08:00–18:00 America/Los_Angeles inclusive."""
    s = start_utc.astimezone(PT)
    e = end_utc.astimezone(PT)
    return (s.hour > 8 or (s.hour == 8 and s.minute >= 0)) and \
           (e.hour < 18 or (e.hour == 18 and e.minute == 0))

# --- TODOs for candidate implementation ---

@app.post("/v1/appointments")
def create_appointment():
    """
    TODO:
    - Validate payload fields and time constraints
    - Enforce 15–120 minute duration
    - Enforce business hours in America/Los_Angeles
    - Reject caregiver overlaps with 409 APPT_OVERLAP
    - Support Idempotency-Key header:
      same key + same body -> return 201 with same data
      same key + different body -> return 409 IDEMPOTENCY_KEY_MISMATCH
    - Return 201 with { id, caregiverId, patientId, start, end } on success
    """
    return err("NOT_IMPLEMENTED", "Implement POST /v1/appointments", 501)


@app.get("/v1/appointments")
def list_appointments():
    """
    TODO:
    - Accept caregiverId, from, to
    - Return items sorted chronologically, with total
      { "items": [{ id, caregiverId, patientId, start, end }], "total": n }
    """
    return err("NOT_IMPLEMENTED", "Implement GET /v1/appointments", 501)
