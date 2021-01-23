import json #Importuje z jsona moje pytania do testu wiedzy
import random #Wyświetlam je losowo
import warnings
warnings.simplefilter('ignore', category=DeprecationWarning)
#Usunięcie warninga Deprecation do funkcji sample (Znalazłam w internecie, że tak się da)
#W innym przypadku, pytania jakie losowałam się powtarzały

def ocena(punkty):
    if punkty < 2:
        return "niedostateczny"
    elif punkty < 4:
        return "dopuszczajacy"
    elif punkty < 6:
        return "dostateczny"
    elif punkty < 8:
        return "dobry"
    elif punkty < 9:
        return "bardzo dobry"
    else:
        return "celujacy"


# def wylosuj_pytanie(pytania): #Wyświetlamy 10 pytań
#     nr_pytania = random.randint(0, len(pytania) - 1)
#     j = 0
#     for pytanie, odp in pytania.items():
#         if j == nr_pytania:
#             return pytanie, odp #krotka
#         j += 1


def quiz(plik_pytania):
    text = open(plik_pytania, "r").read()
    pytania = json.loads(text)
    punkty = 0
    pytania = random.sample(pytania.items(), 10) #Sample-Pytanie się nie powtarzają!
    for pytanie, odp in pytania:
        print(pytanie)
        odpowiedz = input("TAK/NIE").upper() #Mogę pisać z małej litery i to nie będzie błąd
        if odpowiedz == odp:
            punkty += 1
    print(f"Uzyskales ocene: {ocena(punkty)}")


if __name__ == "__main__":
    quiz("pytania.json")