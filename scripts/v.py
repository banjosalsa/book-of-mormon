import json,sys,re
d=json.load(open('data/parsed.json'))
def get(ref):
    m=re.match(r'^(.*?) (\d+):(\d+)(?:-(\d+))?$',ref.strip())
    b,c,a,z=m.group(1).upper(),m.group(2),int(m.group(3)),int(m.group(4) or m.group(3))
    return [(n,t) for n,t,_ in d[f"{b}|{c}"] if a<=n<=z]
for r in sys.argv[1:]:
    for n,t in get(r): print(f"{r.split(':')[0]}:{n} {t}")
    print()
