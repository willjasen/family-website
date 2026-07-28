# Family Website

## Project structure

- `tree/` is the current MacFamilyTree website export. Treat it as generated
  output; it may be replaced in full when a new export is created.
- `index.html` is the hand-maintained landing page. It redirects visitors to
  `tree/index.html` after 10 seconds and provides an immediate link.
- `gtag.html` contains the shared Google Analytics snippet.
- `add_footer.py` injects or refreshes that snippet in the exported HTML.

## After a MacFamilyTree export

1. Export the site into `tree/`.
2. From the repository root, run `python3 add_footer.py`.
3. Verify that `tree/index.html` has one
   `<!-- family-tree-gtag:start -->` marker and that the landing page still
   links to `./tree/index.html`.

## Analytics

- Keep Google Analytics changes in `gtag.html`; do not edit the generated
  snippet in `tree/index.html` directly.
- The site uses hash-based navigation, so retain the initial and `hashchange`
  page-view tracking in `gtag.html`.

## Local preview

Run `python3 -m http.server 8080` from the repository root, then open
`http://localhost:8080/`.

## Git hygiene

- Keep a full MacFamilyTree export replacement separate from hand-maintained
  landing-page or analytics changes when practical.
- Do not commit local caches such as `__pycache__/` or `.DS_Store`.
