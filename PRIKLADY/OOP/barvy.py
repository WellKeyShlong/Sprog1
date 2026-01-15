class Barva:
    def __init__(self, r, g, b):
        if r < 0 or r > 255:
            print("ValeError")
            return False
        if g < 0 or g > 255:
            print("ValeError")
            return False
        if b < 0 or b > 255:
            print("ValeError")
            return False
        
        else:
            self.r = r
            self.g = g
            self.b = b
    
    def __str__(self):
        return f"RGB ({self.r}, {self.g}, {self.b})"
    
    def __add__(self, jina):
        n_r = int((self.r + jina.r)/2)
        n_g = int((self.g + jina.g)/2)
        n_b = int((self.b + jina.b)/2)
        return Barva(n_r, n_g, n_b)
    
    def __mul__(self, nasobek):
        n_r = max(0, min(255, int(self.r * nasobek)))
        n_g = max(0, min(255, int(self.g * nasobek)))
        n_b = max(0, min(255, int(self.b * nasobek)))
        return Barva(n_r, n_g, n_b)
    
    def invertuj(self):
        n_r = 255 - self.r
        n_g = 255 - self.g
        n_b = 255 - self.b
        return Barva(n_r, n_g, n_b)

    def to_hex(self):
        h_r = hex(self.r)
        h_g = hex(self.g)
        h_b = hex(self.b)  
        return f"{h_r[-2:]}{h_g[-2:]}{h_b[-2:]}"

# Test 1: Vytvoření barev
cervena = Barva(255, 0, 0)
zelena = Barva(0, 255, 0)
modra = Barva(0, 0, 255)
print(f"Červená: {cervena}")
print(f"Zelená: {zelena}")
print(f"Modrá: {modra}")

# Test 2: Míchání barev
fialova = cervena + modra
zluta = cervena + zelena
print(f"{cervena} + {modra} = {fialova}")
print(f"{cervena} + {zelena} = {zluta}")

# Test 3: Zjasňování/ztmavování
tmava_cervena = Barva(100, 0, 0)
svetlejsi = tmava_cervena * 2
tmavsi = tmava_cervena * 0.5
print(f"{tmava_cervena} * 2 = {svetlejsi}")
print(f"{tmava_cervena} * 0.5 = {tmavsi}")

# Test 4: Inverze
oranzova = Barva(255, 100, 0)
inv = oranzova.invertuj()
print(f"{oranzova} invertováno = {inv}")

# Test 5: Hex formát
print(f"{cervena} = {cervena.to_hex()}")
print(f"{oranzova} = {oranzova.to_hex()}")


