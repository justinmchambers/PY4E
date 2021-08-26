hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    exit()

if h>40:
    h = (h - 40) * 1.5 + 40

pay = h*r
print(pay)
