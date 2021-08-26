tot = 0
cnt = 0

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
    tot = tot + fval
    cnt = cnt + 1

print(tot,cnt,tot/cnt)
