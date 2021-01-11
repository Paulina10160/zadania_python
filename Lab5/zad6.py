import random
print("Gra 'Za dużo, za mało' ")
randA = int(random.randint(1, 100))
i = 1
while i<=3:

    guessB = int(input("Możesz zgadywać: "))
    if guessB == randA:
        print("Udało Ci się zgadnąć liczbę! Wygrałeś! :) ")
        break
    elif guessB > randA:
        print("Podałeś za dużą liczbę")
    elif guessB < randA:
        print("Podałeś za małą liczbę")

    if i>=3:
        print("------------------------------------")
        print("Niestety przegrałeś, spróbuj ponownie")
        print("Wylosowana liczba to : ", (randA))
    i += 1