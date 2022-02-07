import urllib.request, urllib.parse ,urllib.error
import xml.etree.ElementTree as ET

total = 0
number = 0
count = 0

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1349393.xml"
xml = ''''''
xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)
data = tree.findall('.//count')
for i in data:
    number = int(i.text)
    count += 1
    total += number

print("The sum of the numbers in file: ", total)
print("Number of \"count\" tags:", count)
