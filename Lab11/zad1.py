w = 3 #szerokość pokoju
l = 5 #długość pokoju
h = 2.5 #wysokość pokoju
#S = w+l + 2*(h+l) + 2*(w+h)
S = w*l + 2*(h*l) + 2*(h*w)

print("Ściany i sufit pokoju zajmują ",float(S) , " m^2")

wysokosc_okna = 1.4
szerokosc_okna = 1.7
ilosc_okien = 2
wysokosc_drzwi = 2
szerokosc_drzwi = 0.8
ilosc_drzwi = 1
pow_okna_drzwi = (ilosc_okien*(wysokosc_okna*szerokosc_okna))+(ilosc_drzwi*(wysokosc_drzwi*szerokosc_drzwi))
print("Drzwi i dwa okna zajmują ",float(pow_okna_drzwi ) , "m^2 powierzchni pokoju ")

pow_calkowita = S - pow_okna_drzwi
print("Pokój po odjęci powierzchni drzwi i okien ma", pow_calkowita , "m^2")

