
print("Witam w przeliczniku temperatur!")
wybor = input("Wpisz jakie stopnie chcesz przeliczyć jeśli Kelwiny to wpisz K, jeśli stopnie Celsjusza wpisz C, jeśli stopnie Fahrenheita wpisz F: ")
# ºF na ºC: [ºC]=([ºF]-32)*5/9
#  ºC na ºF: [ºF]=[ºC]*9/5+32
if wybor in ("F", "f",):
    number = float(input("Wpisz liczbę stopni: "))
    licz1 = (number - 32) * 5/9
    print(number, "°F =", round(licz1, 2), "°C")
    if (licz1 <= 0):
        print("Woda zamarza, przy 0 stopniach Celcjusza")
    elif (licz1 >= 100):
        print("Woda wrze przy 100 stopniach Celcjusza, możesz robić herbatkę!")
    licz1_1 = (number - 32) / 1.8000 + 273.15
    print(number, "°F =", round(licz1_1, 2), "K")



elif wybor in ("C", "c",):
    number = float(input("Wpisz liczbę stopni: "))
    licz2 = number * 9/5 + 32
    if (licz2 <= 32):
        print("Woda zamarza przy 32 stopniach Fahrenheita!")
    elif (licz2 >= 212) :
              print("Woda wrze przy 212 stopniach Fahrenheita,więc możesz zrobić herbetę!")
    print(number, "°C =", round(licz2, 2), "°F")
    licz2_2 = number + 273.15
    print(number, "°C =", round(licz2_2, 2), "K")

#℉ =(K - 273.15)* 1.8 + 32.00
elif wybor in ("K", "k",):
    number = float(input("Wpisz liczbę stopni: "))
    licz3_3 = number + -273.15
    print(number, "K =", round(licz3_3, 2), "°C")
    licz3 = (number - 273.15) * 1.8 + 32.00
    print(number, "K =", round(licz3, 2), "℉")
    if (licz3 <= 32):
        print("Woda zamarza przy 32 stopniach Fahrenheita!")
    elif (licz3 >= 212):
        print("Woda wrze przy 212 stopniach Fahrenheita, więc możesz zrobić herbetę!")
        if (licz3_3 <= 0):
            print("Woda zamarza, przy 0 stopniach Celcjusza")
        elif (licz3_3 >= 100):
            print("Woda wrze przy 100 stopniach Celcjusza, możesz robić herbatkę!")

