import pandas as pd
from re import *

xl = pd.read_excel('file.xlsx')

xl_tels = xl['Tel'].tolist()
xl_emails = xl['Email'].tolist()

tels = ''
emails = ''

for i in xl_tels:
 tels += i + ' '

for i in xl_emails:
 emails += i + ' '

comp1 = compile('(\d\s\d\d\d\s\d\d\d\s\d\d\s\d\d)+|(\d\s\d\d\d\s\d\d\d\s\d\d\-\d\d)+|(\d\s[(]\d\d\d[)]\s\d\d\d\s\d\d\s\d\d)+|(\d\s[(]\d\d\d[)]\s\d\d\d\s\d\d\-\d\d)')
list_tels = comp1.findall(tels)

comp2 = compile('\w+\@\w+\.\w+')
list_emails = comp2.findall(emails)

tels = []
emails = list_emails
for i in list_tels:
 for j in i:
  if not(j == ''):
   tels.append(j)


print(tels)
print(emails)