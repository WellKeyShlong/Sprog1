delka_seznamu = int(input("Zadejte délku seznamu: "))

seznam = []

for i in range(delka_seznamu):
    hodnota = int(input(f"Zadejte {i+1}. hodnotu seznamu: "))
    seznam.append(hodnota)

cislo_k_vyhledani = int(input("Zadejte číslo k vyhledání: "))

indexy = [index for index, hodnota in enumerate(seznam) if hodnota == cislo_k_vyhledani]

if indexy:
    print(f"Číslo {cislo_k_vyhledani} se nachází na indexech: {', '.join(map(str, indexy))}")
else:
    print(f"Číslo {cislo_k_vyhledani} v seznamu není.")
