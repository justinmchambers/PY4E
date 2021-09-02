import json
import urllib.request, urllib.parse, urllib.error

address = input('Address? ')
if len(address) < 1 :
    address = 'http://py4e-data.dr-chuck.net/comments_42.json'

#Open json link, read data, extract desired list
print('Retrieving', address)
link = urllib.request.urlopen(address)
data = link.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
comments = info["comments"]

#Loop through list for count + sum it
total = 0
for item in comments:
    cnt = int(item["count"])
    total = total + cnt

print('Sum: ', total)
