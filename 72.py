f = input("Enter a file name:",)
fh = open(f)

cnt = 0
tot = 0

#Searching lines for the spam score and averaging them
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        #print(line)
        sloc = line.find(":")
        val = line[sloc+1:]
        #print(val)
        fval = float(val)
        tot = tot + fval
        #print(tot)
        cnt = cnt + 1
        #print(cnt)
        avg = tot/cnt

print("Average spam confidence:", avg)
