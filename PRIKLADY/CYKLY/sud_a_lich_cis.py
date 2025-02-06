# Načtení čísla jako meze
mez = int(input("Zadejte přirozené číslo jako mez: "))

# Pro každý počet od 1 do zadané meze
for i in range(1, mez + 1):
    if i % 2 == 0:
        print(f"Číslo {i} je sudé.")
    else:
        print(f"Číslo {i} je liché.")