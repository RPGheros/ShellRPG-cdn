# ShellRPG-cdn Assets

Diese Struktur wird aus dem Workspace gespeist.

- `assets/www` enthaelt WWW-relevante oeffentliche Medien
- `assets/client` enthaelt terminalnahe Medienkopien, soweit sie fuer
  oeffentliche Distribution oder spaetere CDN-Nutzung relevant sind
- `ShellRPG-server` und `ShellRPG-www` koennen diese Struktur ueber den
  same-origin `/asset/*`-Pfad mit GitHub-backed Primaerquelle und lokalen
  Fallbacks nutzen

Die Befuellung geschieht ueber `scripts/sync_workspace_assets.py`.
