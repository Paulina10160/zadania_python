i = 0
r_odsetki = 0
while True:
    i += 1
    r_odsetki = (333 + r_odsetki)*1.08
    if i == 12:
        print("Pracownik zgromadzi kwotę: ",r_odsetki)
        break