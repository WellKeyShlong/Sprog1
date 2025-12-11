import math

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __add__(self, jiny):
        nove_x = self.x + jiny.x
        nove_y = self.y + jiny.y
        novy_vektor = Vektor(nove_x, nove_y)
        return novy_vektor
    
    def __sub__(self, jiny):
        nove_x = self.x - jiny.x
        nove_y = self.y - jiny.y
        novy_vektor = Vektor(nove_x, nove_y)
        return novy_vektor
    
    def delka(self):
        delka = math.sqrt(self.x * self.x + self.y * self.y)
        return delka
    
    def __mul__(self, jiny):
        if isinstance(jiny, Vektor):
            vysledek = self.x * jiny.x + self.y * jiny.y
            return vysledek
        
        else:
            nove_x = self.x * jiny
            nove_y = self.y * jiny
            novy_vektor = Vektor(nove_x, nove_y)
            return novy_vektor


# Test 1: Vytvoření vektorů
v1 = Vektor(3, 4)
v2 = Vektor(1, 2)
print(f"v1 = {v1}")  # [3, 4]
print(f"v2 = {v2}")  # [1, 2]

# Test 2: Sčítání
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")  # [3, 4] + [1, 2] = [4, 6]

# Test 3: Odčítání
v4 = v1 - v2
print(f"{v1} - {v2} = {v4}")  # [3, 4] - [1, 2] = [2, 2]

# Test 4: Délka
print(f"Délka {v1} = {v1.delka()}")  # 5.0

# Test 5: Skalární součin
skalarni = v1 * v2
print(f"{v1} · {v2} = {skalarni}")  # 11

# Test 6: Násobení číslem
v5 = v1 * 2
print(f"{v1} * 2 = {v5}")  # [3, 4] * 2 = [6, 8]

# Test 7: Složitější výpočet
v6 = (v1 + v2) * 0.5
print(f"({v1} + {v2}) * 0.5 = {v6}")  # [2.0, 3.0]


#v1 = [3, 4]
#v2 = [1, 2]
#[3, 4] + [1, 2] = [4, 6]
#[3, 4] - [1, 2] = [2, 2]
#Délka [3, 4] = 5.0
#[3, 4] · [1, 2] = 11
#[3, 4] * 2 = [6, 8]
#([3, 4] + [1, 2]) * 0.5 = [2.0, 3.0]