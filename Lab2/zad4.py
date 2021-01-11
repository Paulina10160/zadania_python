a = int(input("Podaj liczbę a :"))

if a < 0:
    print("Podana liczba jest ujemna : a <0 ")
elif a > 0:
    print("Podana liczba jest dodatnia : a > 0")
if (a%2!=0):
    print("Podana liczba jest podzielna przez 2 z resztą")
else:
    print("Podana liczba jest niepodzielna przez 2 z resztą ( Reszta = 0)")