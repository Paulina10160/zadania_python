from math import *
n = int(input("Podaj n: "))
tab9 = []
maxN = 0
p = 1
for i in range (0,n):                           #Przedział od 0 do n (decyduje użytkownik)
    licz = int(input("Podawaj liczby:"))
    tab9.append(licz)                            #Dodaje podaną liczbę (licz) do tablicy
    if licz == maxN:
        p+=1
    if licz>maxN:                                  #Jeśli podana liczba jest większa od maxN (największej liczby), to zamieniamy maxN na licz
        maxN = licz

print("Maksymalna liczba: ",maxN)
print("Wystąpiła {} razy".format(p))