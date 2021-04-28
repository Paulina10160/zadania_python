class Druzyna:
    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto

class Zawodnicy(Druzyna):
    def __init__(self, nazwa, miasto, ilosc_zawodnikow):
        super().__init__(nazwa, miasto)
        self.ilosc_zawodnikow = ilosc_zawodnikow