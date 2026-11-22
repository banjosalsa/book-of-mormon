import json,sys,re
c=json.load(open('data/geo_cands.json'))
book=sys.argv[1].upper(); a=int(sys.argv[2]); z=int(sys.argv[3]); ml=int(sys.argv[4]) if len(sys.argv)>4 else 330
skip=set(sys.argv[5].split(',')) if len(sys.argv)>5 else set()
for k,(sig,t) in c.items():
    m=re.match(r'^(.*) (\d+):(\d+)$',k)
    b,ch,v=m.group(1),int(m.group(2)),int(m.group(3))
    if b==book and a<=ch<=z:
        print(f"{k} [{','.join(sig)}] {t[:ml]}")
