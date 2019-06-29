import re

f = open('Indonesia.txt', 'r', encoding = 'latin1')
teks2 = f.read()
f.close()
p2=r'di\w+'
string = re.findall(p2,teks2)
print(string)
