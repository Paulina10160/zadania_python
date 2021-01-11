x = f"Magia jest w opinii niektórych ucieleśnieniem Chaosu. " \
    f"Jest kluczem zdolnym otworzyć zakazane drzwi. Drzwi, za którymi czai się koszmar, zgroza i niewyobrażalna okropność," \
    f" za którymi czyhają wrogie, destrukcyjne siły, moce czystego zła, mogące unicestwić nietylko tego, kto drzwi te uchyli, " \
    f"ale i cały świat. A ponieważ nie brakuje takich, którzy przyowych drzwiach manipulują, kiedyś ktoś popełni błąd, " \
    f"a wówczas zagłada świata będzieprzesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To," \
    f" że po Koniunkcji Sfer ludzie nauczyli posługiwać się magią, jest przekleństwem i zgubą świata. Zgubą ludzkości." \
    f"Ci, którzy uważają magię za Chaos, nie mylą się."
lower = x.lower()
swap = x.swapcase()
cap = x.capitalize()
replace = x.replace('k', 'a')
lstrip = x.lstrip()
rstrip = x.rstrip()
count = x.count(' ')
find = x.find('a')
isa = x.isalnum()
start = x.startswith("M")
end = x.endswith("a")
print(f"Lower: {lower}")
print(f"Swap: {swap}")
print(f"Cap: {cap}")
print(f"Replace: {replace}")
print(f"Lstrip: {lstrip}")
print(f"Rstrip: {rstrip}")
print(f"Count: {count}")
print(f"Find: {find}")
print(f"Isa: {isa}")
print(f"Start: {start}")
print(f"End: {end}")