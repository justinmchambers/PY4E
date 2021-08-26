#Function to compute overtime pay
def computepay(h,r):
        if h>40:
            h = (h - 40) * 1.5 + 40
        p=h*r
        return p

hs = input("Enter Hours:")
rs = input("Enter Rate:")

#Convert string to float + check valid input
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    exit()

pay = computepay(h,r)
print("Pay", pay)
