# ShellRPG-cdn · v0.7.6

Deutsch | [English](README.en.md)

## Rolle

`ShellRPG-cdn` ist der oeffentliche Asset- und Distributionsendpunkt fuer
kuratiertes ShellRPG-Material. Der Endpunkt liefert keine autoritative
Spielmechanik, sondern dient als Quelle fuer Web- und perspektivisch weitere
public-safe Medienpfade.

## Pflegehinweis

- Bei relevanten Content-, Contract-, Feature- oder Redaktionsaenderungen an
  diesem Endpunkt `README.md`, `README.en.md` und `VERSION` gemeinsam
  aktualisieren.

## Aktueller Stand

- GitHub-backed Primaerpfad fuer WWW-Assets:
  `https://cdn.jsdelivr.net/gh/RPGheros/ShellRPG-cdn@main/assets/www`
- dynv6-Fallback ist fuer lokale bzw. spaetere Deployments vorbereitet
- die eigentliche Asset-Befuellung erfolgt ueber
  `scripts/sync_workspace_assets.py`
- `scripts/sync_workspace_assets.py` verankert aktuelle WWW- und Client-Assets
  als kuratierten CDN-Bestand fuer Server- und WWW-Lieferung

## Wichtig

- Zugangsdaten fuer dynv6 liegen nicht in versionierten Dateien
- reale Tokens gehoeren nur in lokal ignorierte `secrets/`- oder `var/`-Dateien
- ein reiner dynv6-Hosteintrag ist kein echter Multi-Origin-Load-Balancer
- wenn mehrere CDN-Urspruenge gegeneinander geraced werden sollen, muessen
  mehrere konkrete Origin-URLs lokal in `var/asset-origins.toml` oder einer
  vergleichbaren ignorierten Datei hinterlegt werden
- `shell.sh` und `scripts/update_dynv6.py` loesen lokale Secretpfade stabil
  relativ zum CDN-Endpunkt auf
- die Assettaxonomie soll kuenftig auch Monster-, Wildlife-, Material- und
  Ringslot-Ausbaupfade sauber tragen

## Praktische Kommandos

```bash
python scripts/sync_workspace_assets.py
python scripts/update_dynv6.py
./shell.sh
```

`./shell.sh` ist ein schlanker Wrapper fuer den lokalen dynv6-Update-Job.
