class Zajac:
    def __init__(self):
        print('dzień dobry')
        self.numer=2
        print('mam numer',self.numer)
    numer = 0
    kolor = "szary"
    def drukuj(self,materiał):
        print(self.kolor,'zajac na',materiał)
piorun = Zajac()

piorun.drukuj("papier")

class Zajacwyscigowy(Zajac):
    predkosc = 10
    def __init__(self):
        print("wzium")
blyskawica = Zajacwyscigowy()
print(blyskawica.predkosc)