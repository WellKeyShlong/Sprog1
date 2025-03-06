delka = int(input("Zadejte délku seznamu: "))

cisla = []

for i in range(delka):
    cisla.append(int(input(f"zadejte {i+1}. cislo: ")))

dolni_mez = int(input("zadejte dolni mez: "))
horni_mez = int(input("zadejte horni mez: "))

pocet = 0

for cislo in cisla:
    if dolni_mez <= cislo <= horni_mez:
        pocet += 1

print(f"Počet hodnot v intervalu [{dolni_mez}, {horni_mez}] je: {pocet}")
