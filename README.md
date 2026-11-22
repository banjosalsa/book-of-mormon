# Book of Mormon geography web

A study of every direction, distance and place reference in the Book of Mormon, linked into one graph and tested for internal contradictions. Built only from the text in `data/bom.txt`, with no outside maps or commentary and no mapping onto real-world places.

## Result

- 80 places and 109 curated relations, each linked to its verses (95 stated outright, 14 marked inferred).
- No direction loops: 22 north-south and 14 east-west statements are jointly satisfiable, and a solved layout satisfies all of them.
- 17 tests: 12 consistent, 3 minor tensions, 1 naming note, no hard contradictions.
- Minor tensions: the neck's width (Alma 22:32 vs Helaman 4:7), where the Mulekites first landed (Omni 1:16 vs Alma 22:30 and Helaman 6:10), and what Limhi's scouts believed (Mosiah 8:8 vs 21:26).

The text gives few absolute directions and very few numbers, so passing means no contradiction was found, not that the geography is unique.

## Dashboard

`docs/index.html` plus `docs/geo_out.json`: mind map, constraint map, verses by location, tests and method. To view locally: `cd docs && python3 -m http.server`. For GitHub Pages, serve from the `docs/` folder.

## Rebuilding

Run from the repo root:

    python3 scripts/analyze.py      # reads data/parsed.json and scripts/geo_data.py, writes data/ and docs/ geo_out.json

- `scripts/geo_data.py`: curated places and relations with verse references (edit here).
- `scripts/geo_tests.py`: the consistency test write-ups.
- `scripts/parse.py`, `geo_extract.py`, `geo_show.py`, `v.py`: parsing, candidate extraction and verse lookup (`python3 scripts/v.py "ALMA 22:27-34"`).
- `data/bom.txt`, `data/parsed.json`: the text and its parsed form.
