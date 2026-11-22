import json,re,collections
d=json.load(open('data/parsed.json'))
dirw=re.compile(r"\b(north|south|east|west|northward|southward|eastward|westward|northern|southern|eastern|western|north-?west|south-?east|north-?east|south-?west)\b",re.I)
dist=re.compile(r"(journey|day'?s? journey|days'? journey|space of (?:\w+[\s-]*)+(?:days|nights)|(?:one|two|three|four|five|six|seven|eight|nine|ten|twelve|forty|\w+) days?)",re.I)
rel=re.compile(r"\b(borders?|bordering|near(?:er)? (?:the|by|unto)|by the (?:sea|river|seashore|waters)|on the (?:east|west|north|south)|narrow (?:neck|pass|strip|passage)|round about|beyond|between|upon the (?:east|west) sea|seashore|toward|towards)\b",re.I)
mv=re.compile(r"\b(went up|go up|came up|went down|came down|come down|go down|up to the land|down to the land|up into the|down into the|up out of|down out of|up unto|down unto|depart(?:ed)? out of the land|into the wilderness|out of the land of)\b",re.I)
place=re.compile(r"\b(?:land|city|river|waters?|hill|valley|wilderness|sea|mount|plains?|borders?)\b(?: of| called| which was called| by the name of)? ?(?:the )?[A-Z][a-zA-Z\-]+")
cands=collections.OrderedDict()
for k,vs in d.items():
    b,c=k.split('|')
    for n,t,_ in vs:
        sig=[]
        if dirw.search(t): sig.append('dir')
        if re.search(r"journey",t,re.I): sig.append('journey')
        if re.search(r"(days|day's|nights) ?(journey)?",t) and re.search(r"(journey|traveled|travelled|marched|space of)",t,re.I): sig.append('days')
        if rel.search(t) and place.search(t): sig.append('rel')
        if mv.search(t) and place.search(t): sig.append('move')
        if sig: cands[f"{b} {c}:{n}"]=(sig,t)
json.dump(cands,open('data/geo_cands.json','w'))
cnt=collections.Counter(k.rsplit(' ',1)[0] if False else k.split(' ')[0] if not k[0].isdigit() else ' '.join(k.split(' ')[:2]) for k in cands)
print(len(cands))
bycat=collections.Counter(s for sig,_ in cands.values() for s in sig); print(bycat)
