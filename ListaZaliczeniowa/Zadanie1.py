#https://poradnikprzedsiebiorcy.pl/-jak-wyliczac-wynagrodzenia
#ubezpieczenie emerytalne, rentowe, chorobowe, zdrowotne, zaliczka na PIT

#odjęcie od otrzymanego podatku kwoty wolnej od podatku, kwota ta jest ustanowiona ustawowo i jej miesięczna wysokość wynosi 43,76 zł

def oblicz_netto(kwota_brutto):
    emerytalna = 0.0976 * kwota_brutto
    rentowa = 0.015 * kwota_brutto
    chorobowa = 0.0245 * kwota_brutto
    podstwa = kwota_brutto - (emerytalna + rentowa + chorobowa)
    zdrowotna = podstwa * 0.09
    p = emerytalna + rentowa + chorobowa + zdrowotna
    kwota = kwota_brutto - p
    zus_odliczenie = podstwa * 0.0775
    zaliczka = kwota * 0.17 - 43.76 - zus_odliczenie
    if zaliczka < 0:
        zaliczka = 0

    return round(kwota_brutto - (emerytalna + rentowa + chorobowa + zdrowotna + zaliczka), 2)


kwota = float(input("Podaj kwote brutto: "))
print(f"Kwota netto wynosi: {oblicz_netto(kwota)}")