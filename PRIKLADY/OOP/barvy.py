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
        


cervena = Barva(255, 0, 0)
zelena = Barva(0, 255, 0)
fialova = Barva(128, 0, 128)
neplatna = Barva(300, 0, 0)  

print(cervena)   # RGB(255, 0, 0)
print(zelena)    # RGB(0, 255, 0)
print(fialova)   # RGB(128, 0, 128)
print(neplatna)   # ValueError!