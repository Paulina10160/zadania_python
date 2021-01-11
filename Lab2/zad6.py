a = float(input("Podaj liczbę a:"))
b = float(input("Podaj liczbę b:"))
c = float(input("Podaj liczbę c:"))
d = float(input("Podaj liczbę d:"))

if a < b:
    if b > c:
        if ((c > d) or (d > c)):
            print("Liczba B jest  największa")
    elif c > b:
        if c > d:
            print("Liczba C jest  największa")
        elif ((d > c) and (d > b)):
            print("Liczba D jest  największa")
else:
    print("Liczba A jest  największa")