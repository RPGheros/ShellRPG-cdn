# ShellRPG-cdn · v0.7.6

`ShellRPG-cdn` is the public asset and distribution endpoint for curated
ShellRPG media.

## Maintenance Note

- For relevant content, contract, feature, or editorial changes touching this
  endpoint, update `README.md`, `README.en.md`, and `VERSION` together.

- Primary WWW asset base:
  `https://cdn.jsdelivr.net/gh/RPGheros/ShellRPG-cdn@main/assets/www`
- dynv6 fallback is prepared for local and later deployed use
- actual asset population is handled by `scripts/sync_workspace_assets.py`
- `scripts/sync_workspace_assets.py` anchors current WWW and client assets as
  curated CDN content for server and WWW delivery
- real tokens must never be committed; they belong only in ignored local
  `secrets/` or `var/` files
- a single dynv6 host entry is not true multi-origin load balancing
- the future asset taxonomy should also carry monster, wildlife, material, and
  ring-slot expansion paths cleanly
