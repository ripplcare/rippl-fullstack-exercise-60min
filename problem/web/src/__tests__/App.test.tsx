import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import App from "../App";

describe("list renders sorted", () => {
  it("loads and shows sorted items", async () => {
    vi.stubGlobal("fetch", vi.fn(async (url: any) => {
      if (String(url).startsWith("/v1/appointments")) {
        return new Response(JSON.stringify({ items: [
          { id:2, caregiverId:"c1", patientId:"p2", start:"2025-03-10T17:00:00Z", end:"2025-03-10T17:30:00Z" },
          { id:1, caregiverId:"c1", patientId:"p1", start:"2025-03-10T16:00:00Z", end:"2025-03-10T16:30:00Z" }
        ], total:2 }), { status:200 });
      }
      return new Response("not found", { status:404 });
    }) as any);

    render(<App />);
    fireEvent.click(screen.getByText("Load"));
    await waitFor(()=>expect(screen.getByTestId("list").textContent).toContain("p1"));
    const text = screen.getByTestId("list").textContent || "";
    expect(text.indexOf("p1")).toBeLessThan(text.indexOf("p2"));
  });
});
