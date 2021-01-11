x = input("Podaj pierwszy wyraz : ")
n = input("Podaj drugi wyraz : ")

tupla1 = (x)
tupla2 = (n)

list_1 = list(tupla1)
list_2 = list(tupla2)
len_1 = len(list_1) #Sprawdzamy długość podanego wybrazu
len_2 = len(list_2)

print("______________________________________")
print("Długość pierwszego wyrazu to : ", len_1)            #Drukujemy ich długość
print("Długość drugiego wyrazu to : ",len_2)
print("______________________________________")
if len_1 != len_2:
    print("Długość wyrazów nie jest taka sama, więc nie są to anagramy")


i = 0
counter = 0
while i < len(list_1):      #Sprawdzamy czy znak w pierwszym podanym słowie, zajduje się też w drugim
    if list_1[i] in list_2:
        counter+=1
    i+=1
if counter == len_1:
    print("Podane słowa są anagramami")
else:
    print("Podane słowa nie są anagramami! ")

    #anagram to np fosa-sofa albo fura-rufa