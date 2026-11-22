import json, re, sys, math, random, collections, importlib.util

spec = importlib.util.spec_from_file_location('g', 'scripts/geo_data.py')
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
P = json.load(open('data/parsed.json'))

# ---------- verse lookup ----------
def split_ref(ref):
    m = re.match(r'^(.*) (\d+):(\d+)$', ref)
    return m.group(1), int(m.group(2)), int(m.group(3))

VT = {}
for k, vs in P.items():
    b, c = k.rsplit('|', 1)
    for v, t, _ in vs:
        VT[f"{b} {c}:{v}"] = t

def vtext(ref):
    return VT.get(ref)

missing = []
for a, rel, b, n, vs, note, st in g.RELS:
    for r in vs:
        if r not in VT: missing.append(r)
for d, pl, vs, sense in g.UPDOWN:
    for r in vs:
        if r not in VT: missing.append(r)
print("missing refs:", missing)

nodes = {n[0]: dict(id=n[0], label=n[1], region=n[2], kind=n[3]) for n in g.NODES}
for a, rel, b, n, vs, note, st in g.RELS:
    assert a in nodes and b in nodes, (a, b)

# ---------- direction graph / cycle test ----------
def axis_edges(strength_filter=None):
    ns, ew = [], []   # edges (hi, lo, verses, note, a, rel, b); hi is north/east of lo
    for a, rel, b, n, vs, note, st in g.RELS:
        if strength_filter and st not in strength_filter: continue
        if rel == 'N': ns.append((a, b, vs, a, rel, b))
        elif rel == 'S': ns.append((b, a, vs, a, rel, b))
        elif rel == 'E': ew.append((a, b, vs, a, rel, b))
        elif rel == 'W': ew.append((b, a, vs, a, rel, b))
    return ns, ew

def find_cycles(edges):
    adj = collections.defaultdict(list)
    for hi, lo, *_ in edges: adj[hi].append(lo)
    color = {}; stack = []; cycles = []
    def dfs(u):
        color[u] = 1; stack.append(u)
        for w in adj[u]:
            if color.get(w, 0) == 0: dfs(w)
            elif color[w] == 1:
                cycles.append(stack[stack.index(w):] + [w])
        stack.pop(); color[u] = 2
    for u in list(adj):
        if color.get(u, 0) == 0: dfs(u)
    return cycles

def longest_chain(edges):
    adj = collections.defaultdict(list)
    for hi, lo, vs, *_ in edges: adj[hi].append((lo, vs))
    memo = {}
    def lp(u):
        if u in memo: return memo[u]
        best = ([u], [])
        for w, vs in adj[u]:
            sub, sv = lp(w)
            if len(sub) + 1 > len(best[0]): best = ([u] + sub, [vs] + sv)
        memo[u] = best; return best
    out = ([], [])
    for u in list(adj):
        r = lp(u)
        if len(r[0]) > len(out[0]): out = r
    return out

ns_all, ew_all = axis_edges()
ns_x, ew_x = axis_edges({'explicit'})
cyc = dict(ns_all=find_cycles(ns_all), ew_all=find_cycles(ew_all), ns_x=find_cycles(ns_x), ew_x=find_cycles(ew_x))
print("cycles:", {k: len(v) for k, v in cyc.items()})
ns_chain = longest_chain(ns_all); ew_chain = longest_chain(ew_all)
print("NS chain:", ns_chain[0]); print("EW chain:", ew_chain[0])

# ---------- layout (constraint-respecting) ----------
random.seed(7)
ids = [i for i in nodes if nodes[i]['region'] != 'ow']
# initial y by longest-path layering on NS, x by EW
def layers(edges, ids):
    adj = collections.defaultdict(list)
    for hi, lo, *_ in edges: adj[hi].append(lo)
    depth = {}
    def d(u):   # distance from the top
        if u in depth: return depth[u]
        depth[u] = 0
        return depth[u]
    # longest path from sources
    indeg = collections.Counter()
    for hi, lo, *_ in edges: indeg[lo] += 1
    order = []; q = [u for u in ids if indeg[u] == 0]; dd = {u: 0 for u in ids}
    indeg2 = dict(indeg)
    while q:
        u = q.pop(0); order.append(u)
        for w in adj[u]:
            dd[w] = max(dd[w], dd[u] + 1); indeg2[w] -= 1
            if indeg2[w] == 0: q.append(w)
    return dd
dy = layers([e for e in ns_all if e[0] in ids and e[1] in ids], ids)
dx = layers([(lo, hi, *r) for hi, lo, *r in ew_all if hi in ids and lo in ids], ids)  # west -> east
pos = {}
# y grows to the north
reg_anchor = {'nephi': (-0.6, -2.4), 'zar': (-0.2, -0.7), 'east': (1.8, -0.8), 'west': (-2.0, -1.4), 'north': (0.2, 1.0), 'mormon': (0.9, 2.6), 'jared': (-0.9, 2.8)}
for u in ids:
    ax, ay = reg_anchor[nodes[u]['region']]
    pos[u] = [ax + random.uniform(-.6, .6) + 0.25 * dx[u], ay - 0.35 * dy[u] + random.uniform(-.4, .4)]
# y up = north. constraint lists
NSc = [(hi, lo) for hi, lo, *_ in ns_all if hi in ids and lo in ids]
EWc = [(hi, lo) for hi, lo, *_ in ew_all if hi in ids and lo in ids]
springs = []
for a, rel, b, n, vs, note, st in g.RELS:
    if a in ids and b in ids and rel in ('adj', 'in', 'route', 'group', 'days'):
        springs.append((a, b, 0.75 if rel in ('adj', 'in') else 1.15))
for it in range(1500):
    f = {u: [0.0, 0.0] for u in ids}
    for a, b, L in springs:
        dxv = pos[b][0] - pos[a][0]; dyv = pos[b][1] - pos[a][1]
        dist = math.hypot(dxv, dyv) or 1e-3
        k = 0.02 * (dist - L)
        f[a][0] += k * dxv / dist; f[a][1] += k * dyv / dist
        f[b][0] -= k * dxv / dist; f[b][1] -= k * dyv / dist
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            dxv = pos[b][0] - pos[a][0]; dyv = pos[b][1] - pos[a][1]
            dist = math.hypot(dxv, dyv) or 1e-3
            if dist < 0.7:
                k = 0.03 * (0.7 - dist)
                f[a][0] -= k * dxv / dist; f[a][1] -= k * dyv / dist
                f[b][0] += k * dxv / dist; f[b][1] += k * dyv / dist
    for u in ids:
        ax, ay = reg_anchor[nodes[u]['region']]
        f[u][0] += 0.012 * (ax - pos[u][0]); f[u][1] += 0.012 * (ay - pos[u][1])
        pos[u][0] += f[u][0]; pos[u][1] += f[u][1]
    for _ in range(3):
        for hi, lo in NSc:
            gap = pos[hi][1] - pos[lo][1]
            if gap < 0.35:
                s = (0.35 - gap) / 2; pos[hi][1] += s; pos[lo][1] -= s
        for hi, lo in EWc:
            gap = pos[hi][0] - pos[lo][0]
            if gap < 0.35:
                s = (0.35 - gap) / 2; pos[hi][0] += s; pos[lo][0] -= s
viol_ns = [(hi, lo) for hi, lo in NSc if pos[hi][1] <= pos[lo][1]]
viol_ew = [(hi, lo) for hi, lo in EWc if pos[hi][0] <= pos[lo][0]]
print("layout: NS constraints", len(NSc), "violated", len(viol_ns), "| EW constraints", len(EWc), "violated", len(viol_ew))
# normalise to 0..1000 x 0..760 (y flipped for screen)
xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
mnx, mxx, mny, mxy = min(xs), max(xs), min(ys), max(ys)
for u in ids:
    nodes[u]['mx'] = round(60 + 880 * (pos[u][0] - mnx) / (mxx - mnx), 1)
    nodes[u]['my'] = round(40 + 680 * (mxy - pos[u][1]) / (mxy - mny), 1)
# Old World inset: chain left-to-right
ow_order = ['jeru_ow', 'lemuel_ow', 'redsea', 'shazer', 'nahom', 'bounty_ow', 'irreantum', 'promised']
for i, u in enumerate(ow_order):
    nodes[u]['mx'] = 60 + 125 * i; nodes[u]['my'] = 380 + (60 if i % 2 else -60)

# ---------- distance tests ----------
pair_days = collections.defaultdict(list)
for a, rel, b, n, vs, note, st in g.RELS:
    if rel == 'days': pair_days[tuple(sorted((a, b)))].append((n, vs, note))
pair_conf = {k: v for k, v in pair_days.items() if len({x[0] for x in v if x[0] is not None}) > 1}
print("pairs with conflicting day counts:", {k: [x[0] for x in v] for k, v in pair_conf.items()})

# ---------- auto index ----------
PAT = {
 'lemuel_ow': r"valley of Lemuel|valley by the side of a river", 'redsea': r"Red Sea", 'shazer': r"Shazer", 'nahom': r"Nahom",
 'irreantum': r"Irreantum",
 'nephi': r"(?:land|city) (?:of )?(?:Lehi-)?Nephi\b|Lehi-Nephi|land Nephi", 'shilom': r"\bShilom\b", 'shemlon': r"\bShemlon\b",
 'hill_shilom': r"hill[^.]{0,20}north of (?:the land )?Shilom", 'mormon': r"(?:waters|forest|place|land|borders) of Mormon|called Mormon|borders of Mormon",
 'helam': r"(?:land|city) of Helam|\bHelam\b", 'valley_alma': r"valley (?:of |which was called |called )?Alma\b|called the valley Alma", 'amulon': r"land of Amulon|place which was called Amulon",
 'middoni': r"Middoni", 'ishmael': r"land of Ishmael", 'strip': r"narrow strip",
 'zarahemla': r"Zarahemla", 'sidon': r"\bSidon\b", 'sidon_head': r"head of (?:the river )?Sidon", 'gideon': r"(?:land|city|valley) (?:of )?Gideon|valley (?:which was called |called )?Gideon",
 'amnihu': r"Amnihu", 'minon': r"Minon", 'melek': r"\bMelek\b", 'ammonihah': r"Ammonihah", 'noah_l': r"(?:land|city) (?:of )?Noah|borders of Noah", 'sidom': r"\bSidom\b",
 'aaron': r"(?:city|land) (?:which was called |of )?Aaron", 'manti': r"(?:land|city) (?:of )?Manti|borders of Manti|land Manti", 'hermounts': r"Hermounts",
 'east_wild': r"east wilderness", 'south_wild': r"south wilderness",
 'antionum': r"Antionum", 'jershon': r"Jershon", 'moroni_c': r"(?:land|city) (?:of )?Moroni\b", 'nephihah': r"Nephihah", 'lehi_c': r"(?:land|city) (?:of )?Lehi\b|city Lehi|land Lehi",
 'morianton': r"\bMorianton\b", 'omner': r"city of Omner", 'gid': r"city (?:of )?Gid\b", 'mulek_c': r"city (?:of )?Mulek|city Mulek", 'east_sea': r"east sea|sea east",
 'west_sea': r"west sea|sea west", 'zeezrom': r"city (?:of )?Zeezrom", 'cumeni': r"Cumeni", 'antiparah': r"Antiparah", 'judea': r"city (?:of )?Judea",
 'bountiful': r"(?:land|city) (?:of )?Bountiful|land Bountiful|borders of Bountiful", 'desolation': r"(?:land|city) (?:of )?Desolation|land Desolation|city Desolation", 'neck': r"narrow (?:neck|pass|passage)",
 'hagoth': r"Hagoth", 'land_south': r"land southward|south countr|land south\b|southward", 'land_north': r"land northward|north countr|land north\b|northernmost|northward",
 'many_waters': r"many waters|large bodies of water|many rivers",
 'antum': r"\bAntum\b", 'jordan': r"city of Jordan", 'shim': r"hill (?:of )?Shim|hill Shim|hill which shall be called Shim", 'jashon': r"Jashon", 'shem': r"(?:land|city) (?:which was called |of )?Shem\b|land Shem", 'angola': r"Angola",
 'david': r"land of David", 'joshua': r"land of Joshua", 'teancum_c': r"city (?:of )?Teancum|city Teancum", 'boaz': r"city Boaz", 'cumorah': r"Cumorah|hill Ramah",
 'nimrod': r"valley (?:of )?Nimrod|valley Nimrod", 'moriancumer': r"Moriancumer", 'moron': r"land of Moron", 'ablom': r"Ablom", 'ripliancum': r"Ripliancum", 'ogath': r"Ogath",
 'corihor': r"land of Corihor|valley of Corihor", 'shurr': r"valley of Shurr", 'comnor': r"hill Comnor", 'agosh': r"Agosh",
}
DIRW = re.compile(r"\b(north|south|east|west|northward|southward|eastward|westward|northern|southern|eastern|western)\b", re.I)
REL = re.compile(r"\b(borders?|bordering|near|nearer|by the (?:sea|river|seashore|waters)|seashore|narrow|round about|beyond|between|joining|joined|toward|towards|head of)\b", re.I)
MOVE = re.compile(r"\b(went|go|gone|going|come|came|marched?|fled|flee|departed|journey\w*|traveled|returned|carried|brought|sent|retreated|pursued|encamp\w*|pitch\w*)\b", re.I)
UPDN = re.compile(r"\b(up|down)\b", re.I)
DAYS = re.compile(r"\b(days?|journey|years? in the wilderness)\b", re.I)
index = collections.defaultdict(list)
def book_ch(key):
    b, rest = key.rsplit(' ', 1); c, v = rest.split(':'); return b, int(c), int(v)
for key, t in VT.items():
    tt = t.replace('came to pass', '').replace('come to pass', '')
    tags = []
    if DIRW.search(tt): tags.append('dir')
    if REL.search(tt): tags.append('rel')
    if DAYS.search(tt) and re.search(r"journey|traveled|marched|space of|days", tt, re.I): tags.append('dist')
    if UPDN.search(tt) and MOVE.search(tt): tags.append('move')
    elif MOVE.search(tt) and re.search(r"\b(into|unto|towards?|over|out of)\b", tt): tags.append('move')
    if not tags: continue
    b, c, v = book_ch(key)
    for nid, pat in PAT.items():
        if re.search(pat, t):
            # location-word hits for generic direction nodes need an explicit direction signal
            if nid in ('land_north', 'land_south') and 'dir' not in tags: continue
            index[nid].append((key, tags))
# custom: Lamanite Jerusalem (Alma 21-24) and Old World Bountiful/Jerusalem
for key, t in VT.items():
    b, c, v = book_ch(key)
    if b == 'ALMA' and 21 <= c <= 24 and re.search(r"\bJerusalem\b", t): index['jeru_l'].append((key, ['rel']))
    if b == '1 NEPHI' and 2 <= c <= 7 and re.search(r"land of Jerusalem|to Jerusalem|up to the land of Jerusalem", t) and (MOVE.search(t)): index['jeru_ow'].append((key, ['move']))
    if b == '1 NEPHI' and c in (17, 18) and re.search(r"Bountiful", t): index['bounty_ow'].append((key, ['rel']))
    if b == '1 NEPHI' and c == 18 and re.search(r"promised land", t) and re.search(r"arrive|sailed|land", t): index['promised'].append((key, ['move']))
for nid in index:
    seen = set(); lst = []
    for k, tg in index[nid]:
        if k in seen: continue
        seen.add(k); lst.append((k, tg))
    def sk(x):
        b, c, v = book_ch(x[0]); return (list(map(lambda q: q, [b])), c, v)
    index[nid] = lst
print("index sizes:", {k: len(v) for k, v in sorted(index.items(), key=lambda x: -len(x[1]))[:12]})

# ---------- assemble ----------
ev = set()
edges = []
for i, (a, rel, b, n, vs, note, st) in enumerate(g.RELS):
    edges.append(dict(id=i, a=a, b=b, rel=rel, n=n, v=vs, note=note, st=st))
    ev.update(vs)
for d, pl, vs, sense in g.UPDOWN: ev.update(vs)
book_order = ['1 NEPHI','2 NEPHI','JACOB','ENOS','JAROM','OMNI','WORDS OF MORMON','MOSIAH','ALMA','HELAMAN','3 NEPHI','4 NEPHI','MORMON','ETHER','MORONI']
def sortkey(k):
    b, c, v = book_ch(k); return (book_order.index(b) if b in book_order else 99, c, v)
idx_out = {}
for nid, lst in index.items():
    lst = sorted(lst, key=lambda x: sortkey(x[0]))
    idx_out[nid] = [[k, ''.join(t[0] for t in tg)] for k, tg in lst]
    ev.update(k for k, _ in lst)

TESTS_PATH = 'scripts/geo_tests.py'
spec2 = importlib.util.spec_from_file_location('t', TESTS_PATH); t = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(t)
tests = t.build_tests(dict(ns_chain=ns_chain, ew_chain=ew_chain, cyc=cyc, nns=len(ns_all), new=len(ew_all), viol=(len(viol_ns), len(viol_ew)), n_ns_c=len(NSc), n_ew_c=len(EWc),
                           pair_conf={'|'.join(k): [(x[0], x[1], x[2]) for x in v] for k, v in pair_conf.items()}, nodes=nodes, VT=VT, UPDOWN=g.UPDOWN))
for tt in tests:
    for r in tt.get('verses', []): ev.add(r)
    for row in tt.get('rows', []):
        for r in row.get('v', []): ev.add(r)
bad = [r for r in ev if r not in VT]
print("bad refs:", bad)
verses = {k: VT[k] for k in sorted(ev, key=sortkey) if k in VT}
types = collections.Counter(e['rel'] for e in edges)
stats = dict(nodes=len(nodes), edges=len(edges), types=dict(types), verses_embedded=len(verses), indexed_places=len(idx_out),
             ns_constraints=len(ns_all), ew_constraints=len(ew_all), cycles={k: len(v) for k, v in cyc.items()},
             map_violations=dict(ns=len(viol_ns), ew=len(viol_ew)), explicit=sum(1 for e in edges if e['st'] == 'explicit'))
out = dict(regions={k: dict(name=v[0], color=v[1]) for k, v in g.REGIONS.items()}, nodes=list(nodes.values()), edges=edges, verses=verses,
           index=idx_out, tests=tests, stats=stats, updown=[dict(dir=d, place=p, v=vs, sense=s) for d, p, vs, s in g.UPDOWN])
json.dump(out, open('data/geo_out.json', 'w')); json.dump(out, open('docs/geo_out.json', 'w'))
print(stats)
print("tests:", [(x['id'], x['verdict']) for x in tests])
