n = int(input("Podaj ilość (n) liczb: "))
i = 0
for x in range (1, n):
    while i<n:                   #i jest mniejsze od n ( Ilości lczb podanych przez użytkownika )
        i += 1                   #Zwiększamy i o 1
        print("Podaj liczbę: ")
        n = int(input("Podaj liczbe {}: ".format(i)))
        if -6< n <6:
            print("Podana liczba jest z przedziału [-6;6]")
        else:
            print("Podana liczba nie jest z przedziału [-6;6]")
