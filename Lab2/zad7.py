
import math

a = int(input("Podaj wartość a : "))
b = int(input("Podaj wartość b : "))
c = int(input("Podaj wartość c : "))

delta = b*b-4*a*c
print("Delta wynosi ", delta)
if (delta>0):
    x1=(-b-math.sqrt(delta))/2/a                #Pierwiastek to math.sqrt (musimy zaimportować math!)
    x2=(-b+math.sqrt(delta))/2/a
    print("Delta > 0 ")
    print("Równanie ma dwa pierwiastki")
    print("x1=", x1)
    print("x2=", x2)
else:
    if (delta==0):
        x1=-b/(2*a)
        print("Delta = 0 ")
        print("Równanie ma jeden pierwiastek")
        print("x1=", x1)
    else:
      print("Równanie nie ma pierwiastków rzeczywistych, delta jest mniejsza od zera")