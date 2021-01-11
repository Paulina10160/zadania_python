print("Symulator badania alkomatem")


a = float(input("Podaj ilość alkoholu w wydychanym powietrzu(mg/L):"))
b = a * 2.1                                       #X (mg/L) = 2.1 razy X (‰)
print("Wynik w promilach", b, "‰")
if((b == 0.2) or (b < 0.2)):
    print("Jesteś trzeźwy mozesz jechać")
elif (b > 0.2 and b < 2):
    print("Jesteś pijany i nie mozesz jechac")
else :
    print("Jesteś bardzo pijany,lepiej zamów taxi i idź spać")


"""Dopuszczalna ilość alkoholu w ludzkim organizmie, żeby móc legalnie prowadzić pojazd
mechaniczny, to maksymalnie 0,1 mg/l w wydychanym powietrzu"""