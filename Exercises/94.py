f = input("Enter file name")
if len(f) < 1 :
    f = "mbox-short.txt"

fh = open(f)

dnames = dict()

for line in fh:
    if line.startswith('From '):
        line = line.rstrip()
        if len(line) < 1:
            continue
        words = line.split()
        name = words[1]
        dnames[name] = dnames.get(name,0) + 1

topc = None
topn = None

for name,count in dnames.items():
    if topc is None or count > topc:
        topc = count
        topn = name

print(topn, topc)
