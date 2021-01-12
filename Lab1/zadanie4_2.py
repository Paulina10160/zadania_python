#Tutaj znalazłam taki fajny sposów na obliczenie ile w tym momencie mam sekund
import datetime

urodziny = datetime.datetime(2000, 9, 15)
roznica = datetime.datetime.now() - urodziny
print("Mój wiek w sekundach  :")
print(roznica.total_seconds())

#A tutaj udało mi się to nawet w jednej linijce napisać! Jeeeej

print((datetime.datetime.now() - datetime.datetime(2000, 9, 15)).total_seconds())