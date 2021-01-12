#input-możemy pobierać do zmiennej to, co użytkownik wpisze z klawiatury

a = int(input("Podaj liczbe a :"))
b = int(input("Podaj liczbe b :"))

if (a!=0 and b !=0 ):
    plus = int(a) + int(b)
    minus1 = int(a) - int(b)
    minus2 = int(b) - int(a)
    mnoz = int(a) * int(b)
    dzie1 = int(a) / int(b)
    dzie2 = int(b) / int(a)

    print(("Suma:"), plus)
    print(("Różnica(a-b):"), minus1)
    print(("Różnca(b-a)"), minus2)
    print(("Mnożenie:"), mnoz)
    print(("Dzielenie a/b:"), dzie1)
    print(("Dzielenie b/a:"), dzie2)


else:
    print("Jedna z liczb wynosi 0, nie można wykonać dzielenia")


"""Operatory Logiczne
and – oznaczającego, że oba warunki muszą być prawdziwe
or – oznaczającego, że jednen z dwóch warunków musi być spełniony 

a!=0  -  a różne od 0 
a>=0  -  a równe lub większe od 0 """