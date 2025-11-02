import React, { useMemo, useState } from "react";

type Appt = { id:number; caregiverId:string; patientId:string; start:string; end:string };

export default function App() {
  const [caregiverId, setCg] = useState("c1");
  const [items, setItems] = useState<Appt[]>([]);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  async function load() {
    setLoading(true); setErr(null);
    try {
      // TODO: fetch /v1/appointments?caregiverId=... then sort by start
      // const r = await fetch(`/v1/appointments?caregiverId=${encodeURIComponent(caregiverId)}`);
      // const j = await r.json();
      // setItems(j.items.sort((a:Appt,b:Appt)=>a.start.localeCompare(b.start)));
    } catch (e:any) {
      setErr(e.message || "load failed");
    } finally {
      setLoading(false);
    }
  }

  async function onCreate(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setErr(null);
    // TODO: optimistic update + POST to /v1/appointments, rollback on error
  }

  const list = useMemo(()=>items.map(i =>
    <li key={i.id}>{new Date(i.start).toLocaleString()} - {new Date(i.end).toLocaleString()} - {i.patientId}</li>
  ), [items]);

  return (
    <div style={{maxWidth:720, margin:"2rem auto", fontFamily:"system-ui"}}>
      <h1>Caregiver schedule</h1>
      <div>
        <input aria-label="caregiverId" value={caregiverId} onChange={e=>setCg(e.target.value)} placeholder="caregiverId"/>
        <button onClick={load} disabled={loading}>Load</button>
      </div>
      {err && <p role="alert">Error: {err}</p>}
      {loading ? <p>Loading...</p> : <ol data-testid="list">{list}</ol>}
      <h2>Create</h2>
      <form onSubmit={onCreate}>
        <input name="patientId" placeholder="patientId" required />
        <input name="start" placeholder="start ISO UTC" required />
        <input name="end" placeholder="end ISO UTC" required />
        <input name="notes" placeholder="notes" />
        <button type="submit">Create</button>
      </form>
    </div>
  );
}
