name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
mem = dict()
str = ""
handle = open(name)
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line.rstrip()
        words = line.split()
        hours = words[5].split(':')
        mem[hours[0]] = mem.get(hours[0], 0) + 1
lst = sorted(mem.items())
for item in lst:
    print(item[0], item[1])
