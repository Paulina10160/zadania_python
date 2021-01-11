suma = 0        #Suma na początku działania programu = 0
ile = 0
while True:
    a = input("Podaj liczbę:")
    suma = int(suma) + int(a)
    ile += 1
    srednia = suma/ile
    if suma > 100:      #Program skończy działanie gdy suma  będzie większa od 100 (Break)
        print("Suma podanych liczb jest większa od 100, program kończy działanie")
        break
    if srednia == 66:      #Program skończy działanie gdy średnia wyniesie 66 (Break)
        print("Średnia podanych liczb jest równa 66, program kończy działanie")
        break