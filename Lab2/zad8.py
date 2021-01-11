
print("    /|")
print("   / |")
print("c /  |  b")
print(" /   |")
print("/____|")
print("   a  ")
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a*a + b*b == c*c:  #Warunek na trójką prostokątny
    print("Trójkąt jest prostokątny :) ")
else:
    print("Trójkąt nie jest prostokątny :( ")
