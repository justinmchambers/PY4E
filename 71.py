fname = input("Enter a file name:",)
fh = open(fname)

for line in fh:
    line = line.upper().rstrip()
    print(line)
