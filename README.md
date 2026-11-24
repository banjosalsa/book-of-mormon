# Book of Mormon geography web

A study of every direction, distance and place reference in the Book of Mormon, linked into one graph and tested for internal contradictions. Built only from the text in `data/bom.txt`, with no outside maps or commentary and no mapping onto real-world places.

## Result

- 82 places and 118 curated relations, each linked to its verses.
- No direction loops: 22 north-south and 14 east-west statements are jointly satisfiable, and a solved layout satisfies all of them.
- "Up" is always toward Nephi (south) and "down" toward Zarahemla (north) across about 60 verses, so the usage is consistent. The text alone does not settle whether that means elevation, direction or both. The Old World usage ("up" to Jerusalem, "down" into the wilderness) follows elevation and idiom, not compass direction: the Red Sea is south of Jerusalem.
- Only eleven numeric travel times exist in the whole book; only one pair of places gets two different numbers.
- 24 tests: 18 consistent, 1 unresolved tension, 1 minor tension, 4 notes.
  - Tension: Nephihah. Alma 51:25 says Amalickiah would not attack it, 51:26 lists it among cities he took, and Alma 59 has it still Nephite until it falls in the thirtieth year.
  - Minor: the neck's width, a day and a half (Alma 22:32) versus a day (Helaman 4:7), possibly two different lines.

The text gives few absolute directions and very few numbers, so passing means no contradiction was found, not that the geography is unique.

### Second-pass corrections

- Mulekite landing: no longer a tension. Alma 22:31 states the move: "they came from there up into the south wilderness".
- Limhi's scouts (Mosiah 8:8 vs 21:26): not a tension; one verse is hindsight, the other what they believed.
- Alma's route from Mormon to Zarahemla is 8 + 1 + 12 = 21 days, not 20.
- The three days in 1 Nephi 2:6 are not clearly counted from Jerusalem; marked inferred.
- Constraint map: region anchors were inverted, so places without stated directions sat in the wrong half. Fixed.
- Added: Manti on the southern strip by the head of the Sidon (Alma 22:27); the Ether/Mormon route order match; the 3 Nephi destruction check; the Gideon-Manti meeting told twice.

## Approximate Map & Timeline

The map view draws lands as soft colored regions with cities as balls inside them, plus the river Sidon, the east and west seas, the narrow strip of wilderness and the narrow neck. Places are hand-placed in `scripts/map_data.py`; `analyze.py` checks that every stated north/south/east/west relation holds on the map and that every place sits on land. The text gives no borders, so regions are soft areas around their places, and nothing is to scale.

A timeline with seven stops (Jaredites, Lehi & Nephi, Mosiah & Zeniff, Alma, Captain Moroni, Helaman to 3 Nephi, Mormon) shows only the places each era names, colors regions by who holds them, and draws that era's journeys, each with verses.

## Dashboard

`docs/index.html` plus `docs/geo_out.json`: an Overview landing page (the page title links back to it), the Connections Diagram, the Approximate Map & Timeline, Verses by Location (with a key for the direction/distance, border and movement tags), Consistency Tests and Method. The four cards in the header link to the matching tab; the Tensions card jumps to the first tension test. To view locally: `cd docs && python3 -m http.server`. For GitHub Pages, serve from the `docs/` folder.

## Rebuilding

Run from the repo root:

    python3 scripts/analyze.py      # reads data/parsed.json and scripts/geo_data.py, writes data/ and docs/ geo_out.json

- `scripts/geo_data.py`: curated places and relations with verse references (edit here).
- `scripts/geo_tests.py`: the consistency test write-ups.
- `scripts/parse.py`, `geo_extract.py`, `geo_show.py`, `v.py`: parsing, candidate extraction and verse lookup (`python3 scripts/v.py "ALMA 22:27-34"`).
- `data/bom.txt`, `data/parsed.json`: the text and its parsed form.
