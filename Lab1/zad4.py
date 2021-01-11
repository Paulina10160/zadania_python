
import datetime
min = 60
hour = 60
doba = 24
rok = 365
life = 20
secGodz = min * hour
secDoba = secGodz * doba
secRok = secDoba * rok
secLife = secRok * life

print("Sekundy/Godzina=",secGodz,"Sekundy/Doba=",secDoba,"Sekundy/Rok=",secRok,"Sekundy/Life=",secLife)

print("----------------------------------------------")

#Teraz chce zobaczyć ile "aktualnie" mam sekund ( moje życie )

teraz = datetime.datetime.now()
print('Czas systemu operacyjnego: ', teraz)

rok = str(teraz.year)
print('Rok: ', rok)

miesiac = str(teraz.month)
print('Miesiąc: ', miesiac)

dzien = str(teraz.day)
print('Dzień: ', teraz.day)

godzina = str(teraz.hour)
print('Godzina: ', godzina)

minuta = str(teraz.minute)
print('Minuta: ', minuta)

sekunda = str(teraz.second)
print('Sekunda: ', sekunda)

#wiek = godzina * minuta * sekunda * 630720000

#Muszę to jeszcze dopracować