x = int(input("Podaj górną wartość  x: "))
while x !=0:
    x -= 1      #wyrzucanie elementów z listy
    if x % 6 == 0 and x % 9 == 0:
        print(x,'jest podzielne przez 6 oraz 9')
    else:
        print(x)