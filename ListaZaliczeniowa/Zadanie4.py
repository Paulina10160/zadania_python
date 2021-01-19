#https://www.instalki.pl/aktualnosci/hardware/22174-dlaczego-dysk-ma-mniej-gb.html

def prawdziwa_pojemnosc_gb(pojemnosc_producenta_gb):
    bajty = pojemnosc_producenta_gb * 1000000000
    return round(bajty / 1024 / 1024 / 1024, 2) #zaokraglanie do 2 miejsc


gb = float(input("Podaj rozmiar w GB"))
print(f"Faktyczny rozmiar: {prawdziwa_pojemnosc_gb(gb)} GB")