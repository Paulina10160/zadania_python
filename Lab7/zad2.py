import random
tupla2 = []
list_p = []             #El.parzyste
list_np = []            #El.nieparzyste
for i in range (0,100):         #Deklaruje 100 elementową krotkę, wypełnioną randomowo liczbami z przediału (0-10)
    int_rand = int(random.randint(0,10))
    tupla2.append(int_rand)
    i+=1
print(tupla2)
tupla1 = tuple(tupla2)
print(tupla1)
count_0 = tupla2.count(0)       #Sprawdzamy, ile razy wystąpiła liczba 0
count_1 = tupla2.count(1)       #Sprawdzamy, ile razy wystąpiła liczba 1
count_2 = tupla2.count(2)       #Sprawdzamy, ile razy wystąpiła liczba 2
count_0_1 = count_0 + count_1   #Sprawdzamy, ile razy wystąpiła w sumie wystąpiła liczba 0 i 1
print("Liczba 1 oraz 0 wystąpiły: ",count_0_1)
print("Liczba 2 wystąpiła: ",count_2)

for x in range (0,100):
    if tupla1[x] % 2:
        list_np.append(tupla1[x])
    else:
        list_p.append(tupla1[x])

print("Elementy parzyste: ", list_p)
print("Elementy nieparzyste: ", list_np)
print(type(tupla1))

