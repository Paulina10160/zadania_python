#Informacje o listach
"""Deklarowanie niepustej listy z
e zmiennymi typu liczbowego i znakowego
a = [1,2,'tekst',False,True,3.2]
print (a) // wypiszą się elementy zawarte w tablicy czyli 1,2,'tekst',False,True,3.2




Dodanie do tablicy nowej wartości o indeksie a[0]
a[0] = 'ala'
print(a) // wypiszą się elementy ['ala', 2, 'tekst', False, True, 3.2] ponieważ wartość 1 w tablicy zostanie
nadpisana wartością ‘ala’



Odwołania się do indeksów tablic
print (a[0]) // wypisze element o indeksie 0
print (a[1]) //wypisze ostatni element w tablic"""

"""Dodanie nowego elementu na podaną pozycję listy.
Pierwszym argumentem wywołania jest indeks elementu, przed którym nowy element ma zostać
wstawiony: tak więc a.insert(0,3) wstawia na początek listy,
a = [1,2,'tekst',False,True,3.2]
a.insert(0,3)
a.insert(2,-1) print(a)


Dodanie nowego elementu na koniec tablicy a.append(x)
a = [1,2,'tekst',False,True,3.2]
a.append(4)print (a)


Usuwanie pierwszego napotkanego oznaczonego elementu z tablicy
-
a.remove(x)
a = [1,2,'tekst',False,True,3.2]
print (a)
a.remove(2) //usunie wartość 2, która posiada indeks 1
print (a)

Usuwanie elementu o zadanym indeksie
–
a.pop(x)
a = [1,2,'teks
t',False,True,3.2] print(a)
a.pop(2) //usunie wartość ‘tekst’ ponieważ posiada ona indeks 2.
print (a)


Długość listy możemy sprawdzić przy pomocy funkcji len
a = [1,2,'tekst',False,True,3.2] print
(len(a)) //wypisze 6"""