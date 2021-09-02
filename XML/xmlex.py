import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter link: ')
if len(link) < 1 :
    link = 'http://py4e-data.dr-chuck.net/comments_42.xml'

#Open XML link + XPath for all comment counts
url = urllib.request.urlopen(link).read()
comments = ET.fromstring(url)
counts = comments.findall('.//count')
print(counts)

cnt = 0
tot = 0
#Iterate through comment counts and total the comments
for count in counts:
    cnt = cnt + 1
    print('Count: ', cnt)
    print('Comments: ', count.text)
    tot = tot + int(count.text)
print(tot)
