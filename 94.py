f = input("Enter file name")
if len(f) < 1 :
    f = "mbox-short.txt"

fh = open(f)

lnames = list()
dnames = dict()

for line in fh:
    if line.startswith('From '):
        line = line.rstrip()
        if len(line) < 1:
            continue
        words = line.split()
        lnames.append(words[1])

for name in lnames:
    dnames[name] = dnames.get(name,0) + 1

topc = None
topn = None

for name,count in dnames.items():
    if topc is None or count > topc:
        topc = count
        topn = name

print(topn, topc)
