contacts = {
    'Ala': 563810921,
    'Basia': 872320918,
    'Celina': 928463031,
    'Danuta': 916459234,
    'Emilia': 783405815,
    'Fryderyka': 501725316,
    'Gosia': 723013817,
    'Hania': 894311218,
    'Kasia': 903729819,
}
x = len(contacts)
print(contacts)
contacts['Ala'] = 983127324
contacts['Kasia'] = 834174523
print(contacts)
if x % 2 != 0:
    del contacts[x/2]
print(contacts)