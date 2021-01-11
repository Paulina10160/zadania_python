import random
from typing import Set

lotto = set() #przechowuje tylko unikalne wartosci
player = set() #przechowuje tylko unikalne wartosci
while len(lotto)<6:
    x = random.randint(1,49)
    lotto.add(x)

print(lotto)
for i in range(1,7 ):
    player.add(int(input("Kula: ")))
x = 0
isp = lotto.intersection(player) #Część wspólna dwóch zbiorów
print(isp)
if 0<len(isp)<2:
    print("Wygrałeś 100 pln")
elif 2<=len(isp)<4:
    print("Wygrałeś 10000 pln")
elif 4<=len(isp):
    print("Wygrałeś 50000 pln")
elif len(isp) == 6:
    print("Wygrałeś 14312425436524523441344221321410000 pln")
else:
    print("Przegrałeś")