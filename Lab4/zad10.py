a = 0
b = 0
suma = 0
while True:
    a = int(input("Podaj liczbę a : "))
    suma = suma + a
    print(suma)
    if a==b:
        print("Podałeś dwie takie same liczby ", a , ", a suma dodawania to : ",suma)
        break
    b = a