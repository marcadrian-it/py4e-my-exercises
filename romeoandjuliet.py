fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
for line in fh:
    words = words + line.split()
for word in words:
    if word not in lst:
        lst.append(word)
print(sorted(lst))
