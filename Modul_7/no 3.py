import re

f = open('Indonesia.txt', 'r', encoding = 'latin1')
teks3 = f.read()
f.close()
p3=r'di \w+'
string = re.findall(p3,teks3)
print(string)
