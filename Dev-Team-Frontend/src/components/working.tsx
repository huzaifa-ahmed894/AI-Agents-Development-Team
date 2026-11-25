"use client";

import { useEffect, useState } from "react";
import type { Pending } from "@/hooks/use-runs";
import { ROLES } from "./welcome";

// The API returns the finished run only, so we show the real elapsed time, not fake progress.
export function Working({ pending, revising }: { pending: Pending; revising: string | null }) {
  const [seconds, setSeconds] = useState(0);
  useEffect(() => {
    const started = Date.now();
    const timer = setInterval(() => setSeconds(Math.floor((Date.now() - started) / 1000)), 1000);
    return () => clearInterval(timer);
  }, []);
  const elapsed = `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, "0")}`;

  return <div className="working" data-enter>
    <p className="sr-only" role="status">The team is working on your request.</p>
    <p className="eyebrow">{revising ? `Revising ${revising}` : "New project"}</p>
    <h1>{pending.message}</h1>
    <ol className="team-status">
      {ROLES.map(({ icon: Icon, name }) => <li key={name}><span className="pulse" aria-hidden /><Icon size={16} strokeWidth={1.6} aria-hidden />{name}</li>)}
    </ol>
    <p className="muted">The team is working: planning, writing and reviewing. Most runs take one to three minutes.
      <span className="elapsed">{elapsed}</span></p>
  </div>;
}
