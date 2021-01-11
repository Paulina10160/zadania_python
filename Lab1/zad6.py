
s1 = input("podaj dystans w km:")
t1 = input("podaj czas w godzinach:")

v1 = (float(s1)) / (float(t1))                      #Wzór V=S/T

s2 = input("podaj dystans2 w km:")
t2 = input("podaj czas2 w godzinach:")

v2 = (float(s2)) / (float(t2))

zmiana = (float(v2)) - (float(v1))                  #Zmiana prędkości V1-V2

v3 = (v2 + v1) / 2                                 #Średnia prędkość do suma podzielona na dwa

print("Prędkość pierwsza V1:", v1 ,"km/h" )
print("Prędkość druga V2:", v2 ,"km/h")
print("Zmiana prędkości: ", zmiana ,"km/h")
print("Prędkość średnia: ", v3,"km/h")