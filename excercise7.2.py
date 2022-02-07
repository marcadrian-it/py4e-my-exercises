# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    zeropos = line.find('0')
    paragraph = float(line[zeropos - 1:])
    value = value + paragraph
end = str(value / count)
print("Average spam confidence: " + end)
