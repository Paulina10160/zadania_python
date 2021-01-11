tab3 = []       #Tworzymy tablice
i = 0
while i<11:  #Deklarujemy 10 elementów
    a = int(input("Podaj x :  "))
    if a>60 or a<-1:
        print("Musisz podać x z zakresu 0-59")
        continue
    else:
        tab3.append(a)
        i +=1
print(tab3)
insert = 0
while insert < 3:                                           #Dodanie nowego elementu na podaną pozycję listy
    where = int(input("Podaj gdzie chcesz dodać element"))
    what = input("Podaj jaki chcesz dodać element")
    insert += 1
    tab3.insert(where, what)
print(tab3)
append = 0
while append < 3:
    where = int(input("Podaj gdzie chcesz dodać element"))
    what = input("Podaj jaki chcesz dodać element")
    append += 1
    tab3.append(where, what)
print(tab3)
remove = 0
while remove < 3:
    where = int(input("Podaj gdzie chcesz usunąć element"))
    what = input("daj what")
    remove += 1
    tab3.remove(where, what)
print(tab3)
pop = 0
while pop < 3:
    where = int(input("Podaj o jakim indeksie chcesz usunąć element"))
    what = input("daj what")
    pop += 1
    tab3.pop(where, what)
print(tab3)