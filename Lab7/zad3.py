import random

list_np = []
list_p = []
while len(list_np) < 101:               #Krotka 100 elementowa liczb nieparzystych
    int_rand = int(random.randint(0, 100))
    if int_rand % 2 != 0:
        list_np.append(int_rand)

while len(list_p) < 101:                 #Krotka 100 elementowa liczb parzystych
    int_rand = int(random.randint(0, 100))
    if (int_rand % 2) == 0:
        list_p.append(int_rand)


tuplaA = tuple(list_p)
tuplaB = tuple(list_np)
print("Liczby parzyste: ")
print(tuplaA)
print("Liczby nieparzyste: ")
print(tuplaB)

tuplaC = tuplaA + tuplaB
print("Konkatenacja – łączenie ze sobą wyrażeń (w tym przypadku krotek): ")
print(tuplaC)
count_0 = tuplaC.count(0)           #Sprawdzamy ile razy wystąpiło 0
count_100 = tuplaC.count(100)       #Sprawdzamy ile razy wystąpiło 100
print("Liczba 0 wystąpiła: ",count_0)
print("Liczba 100 wystąpiła: ",count_100)
