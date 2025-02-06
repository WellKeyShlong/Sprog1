#hledani perfektniho cisla
for cislo in range(1, 1000):
    delitel = 0
    for i in range(1, cislo):
        if cislo % i == 0:
            delitel += i
    if cislo == delitel:
        print(f"{cislo} je perfektni cislo")