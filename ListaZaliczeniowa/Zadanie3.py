import json
import random


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


def wylosuj_pytanie(pytania):
    nr_pytania = random.randint(0, len(pytania) - 1)
    j = 0
    for pytanie, odp in pytania.items():
        if j == nr_pytania:
            return pytanie, odp #krotka
        j += 1


def quiz(plik_pytania):
    text = open(plik_pytania, "r").read()
    pytania = json.loads(text)
    punkty = 0
    for i in range(10):
        pytanie, odp = wylosuj_pytanie(pytania)
        print(pytanie)
        odpowiedz = input("TAK/NIE")
        if odpowiedz == odp:
            punkty += 1
    print(f"Twoja ocena: {ocena(punkty)}")


if __name__ == "__main__":
    quiz("pytania.json")