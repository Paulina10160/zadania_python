import random

x = int(input("Podaj zakres od: "))
z = int(input("Podaj zakres do: "))
n = int(input("Podaj ile liczb ma być w liście: "))
tab5 = []
for i in range (0, n):
    tab5.append(random.randint(x,z))
print(tab5)
print("3 element od końca {}".format(tab5[-3]))                     #Wyświetla trzeci od końca element listy
k = int(input("Podaj jaki k-element od końca mamy usunąć): "))
tab5.pop(-k)                                                        #Usuwa k-element od końca
print("Tablica po usunięciu ",k ,"elementu : ",tab5)                 #Drukuje tablicę z usuniętym elementem
tab6 = []                                                            #Tworzymy nową tablicę
for i in range (0, n):
    tab6.append(random.randint(x,z))
print("Nowa tablica : ",tab6)
tab7 = sum([tab5, tab6],[])                                          #Nowa tablica 7 ( scalowana 5 i 6 )
print("Scalowane tablice :",tab7)
print("Długość nowej tablicy: ", len(tab7))                           #len-długość tablicy
y = 0
while y<len(tab7):
    z = tab7.count(tab7[y])                                            #.count - zwróci ile razy coś pojawiło się w liście
    if z>1:                                                             #Liczy ile razy powtarza się pierwszy element tablicy
        print("Liczba", tab7[y] ,"powtarza się", z ,"raz/y")            #I potem zwiększa y o 1, czyli liczy ile razy powtarza się 2 element
    y +=z      #y=y+z                                                       #Wykonuje to, aż y == długości tablicy
