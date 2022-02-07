import urllib.request, urllib.parse ,urllib.error

from bs4 import BeautifulSoup
position = 0
total2 = 0
url = input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
while position == 0:
    for tag in tags:
        print('URL:', position, tag.get('href', None))
        position = position + 1
        if position == 18:
            position = 0
            total2 = total2 + 1
            html = urllib.request.urlopen(tag.get('href', None)).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            break
    if total2 == 7:
        break
