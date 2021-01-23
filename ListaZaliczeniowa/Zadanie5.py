def zamien(kwota, typ_waluty, na_dolary):
    przelicznik = {
        "THB" : 0.33,
        "BTC" : 37320,
        "BTN" : 0.14,
        "MRO" : 0.27,
        "ETH" : 1416.12,
        "PLN" : 0.27 #Przeliczam też na Zł
    }
    if typ_waluty in przelicznik:
        if na_dolary:
            return kwota / przelicznik[typ_waluty]
        else:
            return kwota * przelicznik[typ_waluty]
    else:
        return None


def menu():
    odp = input("Czy chcesz zamieniac dolary na inne waluty (TAK/NIE)")
    if odp.upper() == "TAK":
        kwota = float(input("Podaj kwote w dolanach"))
        waluta = input("Na jaka walute chcesz zamienic (THB, BTC, BTN, MRO, ETH, PLN)").upper()
        print(f"{kwota}$ to {zamien(kwota, waluta, True)}{waluta}")
    else:
        waluta = input("Z jakiej waluty chcesz zamienic (THB, BTC, BTN, MRO, ETH, PLN)").upper()
        kwota = float(input(f"Podaj kwote w {waluta}"))
        print(f"{kwota}{waluta} to {zamien(kwota, waluta, False)}$")


menu()



