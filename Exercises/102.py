f = input("Enter file name")
if len(f) < 1 :
    f = 'mbox-short.txt'
fh = open(f)

dtime  = dict()
for line in fh:
    if line.startswith('From '):
        line = line.rstrip()
        if len(line) < 1 :
            continue
        #Finding the time + isolating hours for dictionary
        words = line.split()
        time = words[5].split(':')
        hour = time[0]
        dtime[hour] = dtime.get(hour,0) + 1

for k,v in sorted(dtime.items()):
    print(k,v)
