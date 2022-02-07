import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter url - ")
count = 0
total = 0
data = '''
'''
data = urllib.request.urlopen(url).read()
info = json.loads(data)
print('User count:', len(info))

for item in info['comments']:
    name, count = item['name'], item['count']
    total += count
    print(name, count, total)
print(total)
