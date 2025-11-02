export type Appt = { id:number; caregiverId:string; patientId:string; start:string; end:string };
export async function listAppointments(caregiverId: string): Promise<Appt[]> {
  const r = await fetch(`/v1/appointments?caregiverId=${encodeURIComponent(caregiverId)}`);
  const j = await r.json();
  return j.items;
}
export async function createAppointment(body: {
  caregiverId: string; patientId: string; start: string; end: string; notes?: string;
}) {
  const r = await fetch("/v1/appointments", {
    method: "POST",
    headers: { "Content-Type": "application/json", "Idempotency-Key": (globalThis.crypto?.randomUUID?.() || String(Math.random())) },
    body: JSON.stringify(body)
  });
  if (!r.ok) {
    let msg = `HTTP ${r.status}`;
    try { const j = await r.json(); if (j?.message) msg = j.message; } catch { /* non-JSON */ }
    throw new Error(msg);
  }
  return r.json();
}
