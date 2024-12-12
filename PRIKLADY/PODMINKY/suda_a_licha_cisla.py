
#zadani hodnot
cislo = int(input("Zadejte číslo: "))

zbytek = cislo % 2

if zbytek > 0:
    print("Číslo je liché")
else:
    print("Číslo je sudé")