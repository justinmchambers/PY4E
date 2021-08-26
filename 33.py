sc = input("Enter score:")

try:
    isc = float(sc)
except:
    print("Bad score")
    quit()

if isc > 1.0:
elif isc < 0.0:
    print("Bad Score")
elif isc >= 0.9:
    print("A")
elif isc >= 0.8:
    print("B")
elif isc >= 0.7:
    print("C")
elif isc >= 0.6:
    print("D")
else:
    print("F")
