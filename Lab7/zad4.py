tupla4 = ("a", "b", "c", "abcabc", "bacbac","hutnicza")
slowo = input("daj wyraz: ")
if slowo in tupla4:
    index = tupla4.index(slowo)
    print(index)
