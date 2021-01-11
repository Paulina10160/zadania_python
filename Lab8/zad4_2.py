import json

maile = {}
file = input("Podaj nazwe pliku z danymi")
with open(file, "r") as f: # r - read/odczyt pliku
    dane = f.read() #czyta caly tekst
    maile = json.loads(dane) #zamienia tekst na slownik

print(maile)

odp = input("Czy chcesz wprowadzic adres email? [tak/nie]")
while odp == "tak":
    nazwa = input("Podaj nazwe")
    mail = input("Podaj mail")
    maile[nazwa] = mail
    odp = input("Czy chcesz wprowadzic adres email? [tak/nie]")

#wyswietlamy maile w przyjaznej do przeklejenia formie
odbiorcy = ""
for value in maile.values():
    odbiorcy += value + ","

print(odbiorcy)

#zamiana json na string
doZapisu = json.dumps(maile)

with open(file, "w") as f: #zapis do pliku
    f.write(doZapisu)