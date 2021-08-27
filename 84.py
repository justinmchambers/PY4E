f = input("Enter file name:")
fh = open(f)

#Open file, check for unique words and add to list
lst = list()
for line in fh:
    line = line.rstrip().split()
    for word in line:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
