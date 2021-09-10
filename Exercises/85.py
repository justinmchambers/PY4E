fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
cnt = 0

#Search for email addresses
for line in fh:
    if line.startswith('From '):
        line = line.rstrip()
        if len(line) < 1 :
            continue
        words = line.split()
        print(words[1])
        cnt = cnt + 1
print('There were', cnt, 'lines in the file with From as the first word')
