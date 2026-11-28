Kind: software. A working tool for running an AI development team, not a marketing site.

Direction: a distinctive oxblood workbench with a dark crimson default feel and a warm, paper-like
light theme. Brand actions use garnet red; approval uses a separate muted emerald and drafts use amber.
Errors use orange-red with an icon and text. Display headings use Bricolage Grotesque, interface text
uses Manrope, and code, file names and IDs use JetBrains Mono. There are no serif headlines.

Layout: sidebar (projects → versions) | workspace. A run shows its header (version trail, status,
passes, Download .zip, run ID), then a report column (Summary / Plan / Review as native <details>)
beside a sticky file viewer (tabs, line numbers, highlight.js, copy and download per file).
Below 1100px the report and files stack; below 860px the sidebar becomes a drawer.

Chrome surfaces (sidebar, top bar, composer, dialogs and file tabs) use crimson-tinted translucent
mica with a soft blur and inner highlight. Solid panels remain behind reports and code for readability.
Opaque tinted fallbacks are used when blur is unavailable or reduced transparency is requested.

Shape and elevation: 8px controls, 12px cards, 16px panels and 20px dialogs/composer, with pill badges.
Controls use restrained crimson edge light and soft layered shadows. Focus uses a 2px accent ring.

Layout: the welcome view shows a connected Planner → Developer → Reviewer flow; the working view
shows live role states and a timeline of actual activity events. The run header separates approved and
draft status, and the sidebar shows versions as a timeline with status nodes and short dates.

Truthfulness: no fake streaming or step progress. While the team works, the UI shows only real events
and a real elapsed timer. Errors keep the draft, and POSTs are never retried automatically.

Motion: 150–250ms ease-out feedback, a short entrance and a pulse on the active working role.
prefers-reduced-motion turns motion off; prefers-reduced-transparency disables glass blur.
