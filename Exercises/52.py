smallest = None
largest = None

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    if largest is None:
        largest = fval
    if fval > largest:
        largest = fval
        #print(largest)
    if smallest is None:
        smallest = fval
    if fval < smallest:
        smallest = fval

print("Maximum is", largest)
print("Minimum is", smallest)
