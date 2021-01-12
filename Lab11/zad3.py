import math
kat = int(input("Podaj kąt w stopniach:"))
kat1 = math.radians(kat)
print("Podany kąt w radianach",kat1)             #Przekształca kąt „kat1” ze stopni na radiany.
sin_kat = round(math.sin(kat1), 3 )
cos_kat = round(math.cos(kat1), 3)
tg_kat = round(math.tan(kat1), 3)
ctg_kat = round(1/tg_kat, 3)

if kat == 90:
    tg_kat = "Nie ma czegoś takiego"

print('Sin kąta = ', sin_kat)
print('Cos kąta = ', cos_kat)
print('Tg kąta = ', tg_kat)
print('Ctg kąta = ', ctg_kat)

 #Zaproponuj rozwiązania dla kątów, 70, 90, 35,180, 240,360.
"""
kat70 = 70
kat70_rad = math.radians(kat70)
sin_kat70 = round(math.sin(kat70) , 3 )
.
.
.
analogicznie z tg,cst,cos 
.
.
print(sin_kat70)


i analogicznie robię do innych stopni
 """
