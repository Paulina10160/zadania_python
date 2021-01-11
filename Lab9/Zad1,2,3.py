import random
print('ZADANE 1___*____*______*_____*____  ')
teams = ('Real Madryt', 'A.C. Milan', 'Bayern Monachium', ' Liverpool F.C.', 'FC Barcelona', 'AFC Ajax', ' Manchester United',
         'Juventus F.C.', 'SL Benfica',
         'Borussia Dortmund', 'Chelsea F.C.', 'Feyenoord Rotterdam', ' Aston Villa F.C.', 'Club Brugge', 'Malmö FF',
         'AS Roma', 'U.C. Sampdoria', 'Bayer 04 Leverkusen', ' AS Monaco',
         ' Arsenal F.C.',' Paris Saint-Germain F.C.')
A = {0}
B = {0}
C = {0}                 #Utworzyłam nazwy 4 zestawów
D = {0}
A.remove(0)
B.remove(0)
C.remove(0)             #Usuwam z zespołów 0 ( inaczej nie działa , jak daje A = {} )
D.remove(0)
while len(D) < 10 or len(C) < 10 or len(B) < 10 or len(A) < 10:  #Dopóki ilość 'teams' w zestawach nie będzie równa 10,
    w1 = random.choice(teams)                                    #to dodajemy randomowo(random.choice) teams do zestawu
    w2 = random.choice(teams)
    w3 = random.choice(teams)
    w4 = random.choice(teams)
    if w1 not in A and len(A) < 10:         #Sprawdzamy, żeby nazwy zespołów się nie powtarzały w zestawach
        A.add(w1)
    if w2 not in B and len(B) < 10:
        B.add(w2)
    if w3 not in C and len(C) < 10:
        C.add(w3)
    if w4 not in D and len(D) < 10:
        D.add(w4)
print("Pierwsza drużyna sportowa :  ",A)
print("______________________________________")
print("Druga drużyna sportowa :  ",B)
print("______________________________________")
print("Trzecia drużyna sportowa :  ",C)
print("______________________________________")
print("Czwarta drużyna sportowa :  ",D)
print("______________________________________")

AB = A.intersection(B)              #intersection-część wspólna A i B
CD = C.intersection(D)              #intersection-część wspólna C i D
intersection_set = AB.intersection(CD)
print("Część wspólna pierszej i drugiej drużyny sportowej : ",AB)
print("                                                     ")
print("Część wspólna trzeciej i czwartej drużyny sportowej : " , CD)
print("                                                     ")
print("Część wspólna 1,2,3 i 4 drużyny sportowej : ",intersection_set)
print("")
#zad 2
print('ZADANE 2___*____*______*_____*____  ')
print("")
print('Drużyny, które są w zestawie A ale nie w B: ', A.difference(B))
print('Połączenie zespołów C i D : ',C.union(D))
print('Zwraca wartość true jeśli C jest podzbiorem A: ',A.issuperset(C))
print("")
#zad 3
print('ZADANE 3___*____*______*_____*____  ')
print("")
print("Długość pierwszej drużyny : ",len(A))
print("Długość drugiej drużyny: ",len(B))
print("Długość trzeciej drużyny: ",len(C))
print("Długość czwartej drużyny: ",len(D))

if 'Real Madryt' in A:          #Jeśli Real Madryt pojawi się w pierwszej drużynie, to usuń Real Madryt
    A.remove('Real Madryt')
print(A)

A_list = list(A)        #Konwersujemy zestaw na listę
print(A_list)