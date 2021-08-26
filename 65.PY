text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(':')
num = text[pos:]
nnum = num.strip()
fnum = float(nnum)
print(fnum)
