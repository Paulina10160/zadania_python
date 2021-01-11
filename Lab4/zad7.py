licz = int(input("Podaj liczbę: "))
i = 2
while licz > 0:
    if licz == 2:
        print(licz,"To jest liczba pierwsza")
        break
    elif licz % i == 0:
        print(licz,"To nie jest liczba pierwsza")
        break
    else:
        print( licz,"To jest liczba pierwsza")
        break

"""liczba pierwsza
 – to liczba naturalna większa od siebie, która ma dokładnie dwa dzielniki naturalne –1
oraz samą siebie."""