a = int(input("Podaj liczbę a:"))
b = int(input("Podaj liczbę b:"))
if ((a==0) or (b == 0)):
    print("Jedna z podanych liczb wynosi 0, nie można wykonać dzielenia")

elif (a%b == 0):
    print("A JEST PODZIELNE PRZEZ B")

else:
    print("A NIE JEST PODZIELNE PRZEZ B")


