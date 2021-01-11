
a = float(input("Podaj liczbę a:"))
b = float(input("Podaj liczbę b:"))
c = float(input("Podaj liczbę c:"))
if (a == b):
    print("Liczby są równe : a = b")
elif (a == c):
    print("Liczby są równe : a = c")
elif (b == c):
    print("Liczby są równe : b = c")
elif a < b:
    if b > c:
        print("Największa jest liczba b")
    else:
        print("Największa jest liczba c")
elif a > b:
    if a > c:
        print("Największa jest liczba a")
    else:
        print("Największa jest liczba c ")