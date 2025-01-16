import math

#import cisel
a = int(input("Zadejte koeficient a: "))
b = int(input("Zadejte koeficient b: "))
c = int(input("Zadejte koeficient c: "))

diskriminant = float((b ** 2) - (4*a*c))

if diskriminant >=0:
    kořen1 = float((-b + math.sqrt(diskriminant)) / 2*a)
    kořen2 = float((-b - math.sqrt(diskriminant)) / 2*a)
    print(f"Kořeny rovnice jsou x1 = {kořen1}, x2 = {kořen2}")
else:
    print("Rovnice v R nemá řešení!!")