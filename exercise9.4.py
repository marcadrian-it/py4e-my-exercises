name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()
handle.read()
for line in handle:
    if not line.startswith('From '):
        continue
    else:
        sender = line.split()
        emails[sender[1]] = emails.get(sender[1], 0) + 1
max_value = None
big_word = None
for word, num in emails.items():
    if (max_value is None or num > max_value):
        max_value = num
        big_word = word

print(big_word, max_value)
