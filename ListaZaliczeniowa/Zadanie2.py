from Zadanie1 import oblicz_netto  # Korzystam z zadania 1 , żeby obliczyć ile netto zarabiam


# https://smeo.pl/blog/rozwoj-biznesu/koszty-pracodawcy-w-5-krokach/

def koszt_pracodawcy(pensja_brutto):
    emerytalne = pensja_brutto * 0.0976
    rentowa = pensja_brutto * 0.065
    wypadkowa = pensja_brutto * 0.0167
    fundusz = pensja_brutto * 0.0245
    fgsp = pensja_brutto * 0.01
    return pensja_brutto + emerytalne + rentowa + wypadkowa + fundusz + fgsp


if __name__ == "__main__":
    brutto = float(input("Podaj kwotę brutto zarobkow: "))
    print(f"Lacznie pracodawca wydal na Ciebie: {koszt_pracodawcy(brutto)}zl")
    print(f"Zarabiasz netto: {oblicz_netto(brutto)} zł")
