# NEEPC website

Site for the New England Economics PhD Students Conference, hosted by the Brown Economics GSA. Live at https://neepc.github.io

Plain HTML and CSS, no build step. Edit the .html files and push to `main`; GitHub Pages republishes in about a minute.

- Styles: `assets/css/style.css`
- Images: `assets/img/`
- Anything highlighted yellow on the site (`class="tba"`) is a placeholder still to fill in.

## Past conference programs

`past.html`, `2025.html`, `2026.html` are generated. Don't edit them by hand:

1. Edit the data in `_build/programs.py` (add a new year by copying an existing one).
2. Run `python3 _build/build_past.py` from the repo root.
3. If you add a year, also add it to the Past Conferences dropdown (`<ul class="sub">`) in every page's header.

Folders starting with `_` are not published by GitHub Pages.
