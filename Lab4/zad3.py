while True:                                      #Warunek pętli będzie wykonywał się w nieskończoność (true)
    x = int(input("Podaj liczbe: "))
    if x % 12 == 0:                              #Aż znajdziemy x podzielnego przez 12
        print("Podałeś liczbę podzielną przez 12, czyli ",x , " ,wiec kończę działanie pętli")
        break