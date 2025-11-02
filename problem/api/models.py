from sqlalchemy import Column, Integer, String, DateTime, Index
from .db import Base

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    caregiver_id = Column(String, nullable=False, index=True)
    patient_id = Column(String, nullable=False)
    start_at = Column(DateTime(timezone=True), nullable=False, index=True)
    end_at = Column(DateTime(timezone=True), nullable=False)
    notes = Column(String)

Index("uix_caregiver_start", Appointment.caregiver_id, Appointment.start_at, unique=True)
