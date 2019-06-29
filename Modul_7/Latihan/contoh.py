import re

string = "sebuah kata pada semangka yg berjumlah sebanyak mungkin"

pola = r"se\w+"

tampilan = re.findall(pola,string)
print(tampilan)



string2 = "di sini ada kambing, di sana ada buaya, dan disitu ada mantan"

pola2 = r"di \w+"

tampilan2 = re.findall(pola2,string2)
print(tampilan2)
