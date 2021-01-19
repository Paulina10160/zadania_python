# import random
#
#
#
# def wyswietl(slowo, ile_razy):
#     for i in range(ile_razy):
#         print(slowo)


# wyswietl("lol", 15)
# wyswietl("slowo", 3)
#
#
# def losuj(n):
#     wynik = []
#     for i in range(n):
#         a = random.randint(0, 10)
#         wynik.append(a)
#     return wynik
#
#
# lista = losuj(7)
# lista2 = losuj(12)
# print(lista)
# print(lista2)
#

def czy_przestepny(R):
    if R % 4 == 0 and R % 100 != 0:
        return True
    elif R % 400 == 0:
        return True
    else:
        return False


#Latami przestępnymi są te, których numeracja jest podzielna przez 4 i niepodzielna przez 100 lub jest podzielna przez 400.
def pobierz_miesiace(R):
    luty = 28
    if czy_przestepny(R):
        luty = 29
    miesiace = [31, luty, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return miesiace


def data_jutro(D, M, R):
    miesiace = pobierz_miesiace(R)
    nowy_rok = R
    nowy_miesiac = M
    nowy_dzien = D + 1
    if nowy_dzien > miesiace[M - 1]:
        nowy_miesiac = M + 1
        if nowy_miesiac > 12:
            nowy_rok = R + 1
            nowy_miesiac = 1
        nowy_dzien = 1
    return nowy_dzien, nowy_miesiac, nowy_rok


def data_wczoraj(D, M, R):
    miesiace = pobierz_miesiace(R)
    nowy_rok = R
    nowy_miesiac = M
    nowy_dzien = D - 1 #przesuwamy sie o jeden dzien do tylu
    if nowy_dzien == 0: #jesli mamny np 1 stycznia to przechodzimy na poprzedni miesiac (a nawet rok)
        nowy_miesiac = M - 1 #przesuwamy sie na poprzedni miesiac
        if nowy_miesiac == 0: #przesuwamy sie na poprzedni rok
            nowy_rok = R - 1
            nowy_miesiac = 12
            nowy_dzien = 31
        else:
            nowy_dzien = miesiace[nowy_miesiac-1]
    return nowy_dzien, nowy_miesiac, nowy_rok


#http://cybermoon.pl/wiedza/algorithms/wielkanoc.html
def wielkanoc(y):
    a = y % 19
    b = y % 4
    c = y % 7
    d = (19*a + 24) % 30
    e = (2*b+4*c+6*d+5) % 7
    dayMar = 22 + d + e
    dayApr = d + e - 9
    if dayMar > 31:
        return dayApr, 4, y
    else:
        return dayMar, 3, y


#https://mattomatti.com/pl/a0041
def dzien_tygodnia(D, M, R):
    miesiace = [0, 3, 3, 6, 1, 4 , 6 ,2, 5, 0, 3, 5]
    #// - dzielenie calkowite
    q = (R - 1) // 4 - (R - 1)//100 + (rok - 1)//400
    p = (R - 1) + q
    p += miesiace[M - 1]
    if M > 2 and czy_przestepny(R):
        p += 1
    p += D - 1
    return p % 7


def data(D, M, R):
    wczoraj = data_wczoraj(D, M, R)
    print(f"Wczoraj bylo: {wczoraj}")
    jutro = data_jutro(D, M, R)
    print(f"Jutro bedzie: {jutro}")
    w = wielkanoc(R)
    print(f"Wielkanoc wypada w: {w}")
    dni = ["pon", "wt", "sr", "czw", "pt", "so", "nd"]
    nr_dnia = dzien_tygodnia(D, M, R)
    print(f"Dzien tygodnia: {dni[nr_dnia]}")


if __name__ == "__main__":
    print("Podaj date:")
    dzien = int(input("Podaj dzien"))
    miesiac = int(input("Podaj miesiac"))
    rok = int(input("Podaj rok"))
    data(dzien, miesiac, rok)