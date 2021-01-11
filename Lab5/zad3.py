n = int(input("Podaj liczbę którą mam odwrocić: "))
tyl = int(str(n)[::-1])    #Funkcja, która odwraca kolejność  znaków
if int(tyl) == n:
    print("Podana liczba", tyl, "jest palindromem")
else:
    print("Podana Liczba",n,", po odwróceniu : " ,tyl)



"""Palindrom tzn. czytana od końca jest taka sama """