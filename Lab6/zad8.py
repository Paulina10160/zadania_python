import random

randomList = random.sample(range(0,50), 10)   #Program losuje 10 liczb z przedziału (0,50)
print("Lista przed zmieszaniem: ", randomList)
random.shuffle(randomList)                    #Program miesza naszą listę
print("Pomieszana lista: ", randomList)
randomList.sort()                              #Program sortuje naszą listę (Od najmniejszej do największej)
print("Posortowana lista:", randomList)
