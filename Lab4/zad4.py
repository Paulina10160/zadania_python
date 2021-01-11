liczba = -1
suma = 0
ile = -1
while liczba != 0:
    liczba = int(input("Podaj liczbe: "))
    suma += liczba
    ile += 1

if ile == 0:
    print("Nie wprowadzono danych")
else:
    print(suma/ile)


#jesli user poda cos innego niz liczba to mozna by zrobic na instrukcji wczytywania i konwersji blok try a w except wpisac np brek