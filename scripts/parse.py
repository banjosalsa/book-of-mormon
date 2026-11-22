import re, sys, json, collections
lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
hdr = re.compile(r'^((?:[1-4] )?[A-Z][A-Z ]+?)(?: (\d+))?$')
books = []
cur = None
data = collections.OrderedDict()
issues = []
curkey=None
for i,l in enumerate(lines,1):
    if not l.strip(): continue
    m = re.match(r'^((?:[1-4] )?(?:NEPHI|[A-Z][A-Z ]+?)) (\d+)$', l)
    if m and l.upper()==l:
        curkey=(m.group(1), int(m.group(2))); data[curkey]=[]; continue
    m = re.match(r'^(\d+) (.*)$', l)
    if m and curkey:
        data[curkey].append((int(m.group(1)), m.group(2), i)); continue
    if curkey and l.upper()!=l or (curkey and not re.match(r'^[A-Z0-9 ]+$', l)):
        issues.append((i,'nonverse',l[:100]))
    elif l.upper()==l:
        pass
json.dump({f"{k[0]}|{k[1]}":[(a,b,c) for a,b,c in v] for k,v in data.items()}, open('data/parsed.json','w'))
# verse continuity
prevbook=None
for (b,c),vs in data.items():
    nums=[v[0] for v in vs]
    exp=list(range(1,len(nums)+1))
    if nums!=exp:
        issues.append((vs[0][2] if vs else 0,'verse-seq',f"{b} {c}: {nums[:5]}...{nums[-5:]} len={len(nums)}"))
    if not vs: issues.append((0,'empty',f"{b} {c}"))
# chapter continuity
bk=collections.defaultdict(list)
for (b,c) in data: bk[b].append(c)
for b,cs in bk.items():
    if cs!=list(range(1,len(cs)+1)): issues.append((0,'chapter-seq',f"{b}: {cs}"))
    print(b, len(cs), 'chapters', sum(len(data[(b,c)]) for c in cs),'verses')
print(len(issues),'issues')
for x in issues[:80]: print(x)
