contacts = {
    'St. Louis Pizza': 11,
    '(Buffalo) Mozzarella cheese': 22,
    'Neapolitan Pizza': 31,
    'Detroit Pizza': 14,
    'Sicilian Pizza': 15,
    'Deep-Dish Pizza': 16,
    'New York-Style Pizza': 17,
    'Californian Pizza': 18,
    'BBQ chicken': 19,
    'Greek Pizza': 32
}
for keys in contacts.keys():        #Wypisuje klucze
    print(keys)

for values in contacts.values():    #Wypisuje wartości
    print(values)

for items in contacts.items():      #Wypisuje klucze i wartości
    print(items)
#Mamy możliwość dodania nowej pozycji do karty
key = input("Podaj nazwe: ")
value = float(input("Podaj cene: "))
contacts[key] = value

"""Usuwa elementy o najniższej i najwyższej cenie"""
max_v = max(contacts.values())
min_v = min(contacts.values())
max_k = max(keys for keys, values in contacts.items() if values == max_v)
min_k = min(keys for keys, values in contacts.items() if values == min_v)

del contacts[max_k]
del contacts[min_k]

print(contacts)