n = int(input("Podaj liczbę, z której chcesz obliczyć silnię: "))
i = 1
for a in range (1, n+1):
    i = i*a
print("Silnia z liczby ",n," to ",i)