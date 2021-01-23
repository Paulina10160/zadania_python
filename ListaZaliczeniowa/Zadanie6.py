#C K F N
def na_kelwina(value, jednostka):
    if jednostka == 'C':
        return value + 273.15
    elif jednostka == 'K':
        return value
    elif jednostka == 'F': # (°F + 459.67) × 5/9
        return (value + 459.67) * (5/9)
    elif jednostka == 'N': #°C = °N × 100/33
        return value * 100/33 + 273.15
    else:
        return None


def na_celsjusza(value, jednostka):
    if jednostka == 'C':
        return value
    elif jednostka == 'K':
        return value - 273.15
    elif jednostka == 'F': #°C = (°F − 32) /1.8
        return (value - 32) * 5/9
    elif jednostka == 'N': #°C = °N × 100/33
        return value * 100/33
    else:
        return None


def na_fahrenheita(value, jednostka):
    if jednostka == 'C': #°F = (°C × 1.8) + 32
        return value * 1.8 + 32
    elif jednostka == 'K': # 	°F = (K × 1.8) - 459.67
        return (value * 1.8) - 459.67
    elif jednostka == 'F':
        return value
    elif jednostka == 'N': #°F = °N × 60/11 + 32
        return value * 60/11 + 32
    else:
        return None


def na_newtona(value, jednostka):
    if jednostka == 'C': # 	°N = °C × 33/100
        return value * 33/100
    elif jednostka == 'K':
        return (value - 273.15) * 33/100
    elif jednostka == 'F': # (°F − 32) × 11/60
        return  (value - 32) * 11/60
    elif jednostka == 'N':
        return value
    else:
        return None


def celsjusz(licz1):
    if licz1 <= 0:
        print("Woda zamarza, przy 0 stopniach Celcjusza")
    elif licz1 >= 100:
        print("Woda wrze przy 100 stopniach Celcjusza, możesz robić herbatkę!")


def farenheit(licz2):
    if licz2 <= 32:
        print("Woda zamarza przy 32 stopniach Fahrenheita!")
    elif licz2 >= 212:
        print("Woda wrze przy 212 stopniach Fahrenheita,więc możesz zrobić herbetę!")


def kelwin(licz2):
    if licz2 <= 273:
        print("Woda zamarza przy 273 stopniach Klewina!")
    elif licz2 >= 373:
        print("Woda wrze przy 373 stopniach Klewina,więc możesz zrobić herbetę!")


def newton(licz2):
    if licz2 <= 0:
        print("Woda zamarza przy 32 stopniach Newton!")
    elif licz2 >= 303.03:
        print("Woda wrze przy 303.03 stopniach Newtona,więc możesz zrobić herbetę!")


def main():
    wybor = input("Podaj w jakiej jednostce wprowadzasz temperature C, K, F, N: " ).upper()
    value = float(input("Podaj wartosc temperatury: "))

    F = round(na_fahrenheita(value, wybor), 2)
    C = round(na_celsjusza(value, wybor), 2)
    N = round(na_newtona(value, wybor), 2)
    K = round(na_kelwina(value, wybor), 2)

    print(f"{value} stopni {wybor} to {F} stopni F")
    print(f"{value} stopni {wybor} to {K} stopni K")
    print(f"{value} stopni {wybor} to {C} stopni C")
    print(f"{value} stopni {wybor} to {N} stopni N")

    celsjusz(C)
    farenheit(F)
    kelwin(K)
    newton(N)


main()