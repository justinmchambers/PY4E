# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL? ')
cycs = int(input('Cycles? '))
pos = int(input('Position? '))

#Loop for desired cycles
while cycs > 0 :
    cycs = cycs - 1
    #Use BS to pull tags
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #Select the desired tag from list + open it
    link = tags[pos-1]
    url = link.get('href', None)
    print(url)
