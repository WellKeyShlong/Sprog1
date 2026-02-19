import math

def kvadraticka_rovnice(a, b, c):
    diskriminant = float((b ** 2) - (4*a*c))

    if diskriminant <0:
        return None
    else:
        x1 = float((-b + math.sqrt(diskriminant)) / 2*a)
        x2 = float((-b - math.sqrt(diskriminant)) / 2*a)
        return x1, x2

# Příklad použití
print(kvadraticka_rovnice(1, -5, 6))  # Očekávaný výstup: (3.0, 2.0)
print(kvadraticka_rovnice(1, -4, 4))  # Očekávaný výstup: (2.0, 2.0)
print(kvadraticka_rovnice(1, 2, 5))   # Očekávaný výstup: None