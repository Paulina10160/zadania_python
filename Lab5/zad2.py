import statistics
n = int(input("Podaj zakres od (x) : "))
x = int(input("Podaj zakres do (n) : "))
nFor = n-1
i = 0                   #Na początku wszystko ma wartość wejściową 0
sumaN = 0
sredniaN = 0
minN = 0
maxN = 0
medianaN = 0
listaM  =[]
for y in range (n,n+6):
    nFor += 1
    i += 1
    if x == 0 or x < n:
        print("Podany zakres jest nieprawidłowy x=0 lub x<n")
    else:
        print(i," element: ", nFor)         #Wypisujemy pierwsze 6 liczb z podanego przedziału
        listaM.append(nFor)
        sumaN = sumaN + nFor
        minN = min(n,nFor)
        maxN = max(n,nFor)
        medianaN = statistics.median(listaM)


print("Minimalna liczba to {}".format(minN))
print("Maksymalna liczba to {}".format(maxN))
print("Średnia liczb to {}".format(sumaN/6))
print("Mediana liczb to {}".format(medianaN))