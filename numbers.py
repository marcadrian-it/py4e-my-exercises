import re
name = input('Enter file name:')
if len(name) < 1:
    name = 'actual_data.txt'
handle = open(name)
total = 0
for line in handle:
    x = re.findall("[0-9]+", line)
    for i in x:
        total += int(i)
print(total)


#total = 0


# 417209

# Logics

# To start with, try using with when you do open so that once any job is done, open is closed.

# Following lines are removed as they seemed redundant:

# count = count+1: Not used.
# line = line.rstrip(): re.findall takes care of extraction, so you don't have to worry about stripping lines.

# if len(x)!= 1 : continue: Seems like you wanted to skip the line with no digits. But since sum(map(int, re.findall("\d+", line))) returns zero in such case, this is also unnecessary.

# num = int(x[0]): Finally, this effectively grabs only one digit from the line. In case of two or more digits found in a single line, this won't serve the original purpose. And since int cannot be directly applied to iterables, I used map(int, ...).
