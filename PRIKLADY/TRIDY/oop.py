class Hrac:
    #konstruktor
    def __init__(self, name):
        #atributy
        self.jmeno = name
        self.zivot = 100
        self.penize = 20

    #metody
    def utrzi_zraneni(self, dmg):
        self.zivoty -= dmg

hrac1 = Hrac("David")

odmena = 150
print(hrac1.penize)
hrac1.penize=odmena
print(hrac1.penize)
