class Student:
    def init(self,napoj,przekaska,komputer,wieza,planszowki):
        self.napoj = napoj
        self.przekaska = przekaska
        self.komputer = komputer
        self.wieza = wieza
        self.planszowki = planszowki
    def picie(self):
        print("Pijemy napój, ",self.napoj," jest pyszna!")
    def jedzonko(self):
        print("Pyszne ",self.przekaska,". Yummi!")
    def komputron(self):
        print(self.komputer," rusza! SZYKOWAĆ SIĘ!")
    def glosniki(self):
        print("Odpalamy głośniki!",self.wieza)
    def planszowka(self):
        print("Gramy w planszówkę! Dzisiaj: ",self.planszowki)
Michal = Student("Herbatka","Orzeszki w panierce","Potężna maszyna","Sven odbiór!","Eldritch Horror")
Michal.picie()
Michal.jedzonko()
Michal.komputron()
Michal.glosniki()
Michal.planszowka()