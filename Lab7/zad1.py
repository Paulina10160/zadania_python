tupla1 = ('pies',4,5,3,'kot','rybka')

print(tupla1)
print(id(tupla1))               #Sprawdzamy jej miejsce w pamięci
tupla1 = tupla1 + ('szpinak', 7)
print(id(tupla1))
print(tupla1)

tupla_1 = list(tupla1)
print("Krotka zamieniona na listę: ")
print(tupla_1)