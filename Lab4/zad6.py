i = 2
sum = 1
n = int(input("Podaj liczbę: "))
while (i <= n//2 ):
    if (n % i == 0):
        sum += i
        i += 1
if sum == n:
        print(n,"jest liczbą doskonałą")
else:
        print(n,"nie jest liczbą doskonałą")

"""Liczba
doskonała, to taka liczba, która jest sumą wszystkich swoich dzielników właściwych (czyli
mniejszych od niej samej)."""