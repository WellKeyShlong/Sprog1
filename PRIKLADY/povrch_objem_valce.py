import math

#vyska, polomer
vyska = int(input("Zadejte vysku valce: "))
polomer = int(input("Zadejte polomer valce: "))

#vypocet objemu a povrchu
print(f"objem valce je: {round(math.pi * polomer ** 2 * vyska, 2)}")
print(f"povrch valce je: {2 * math.pi * polomer * (polomer + vyska)}")
