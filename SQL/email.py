import sqlite3
import re

conn = sqlite3.connect('email.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

f = input('File name? ')
if len(f) < 1 :
    f = 'mbox-short.txt'
fh = open(f)

for line in fh:
    if not line.startswith('From: '):
        continue
    words = line.split()
    email = words[1]
    orgl = re.findall('.*@(.+)', email)
    for org in orgl:
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
        else:
            cur.execute('''UPDATE Counts SET count = count + 1
                    WHERE org = ?''', (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()
