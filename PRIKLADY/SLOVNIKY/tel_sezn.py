#tel seznam

seznam = {}

kont = int(input("Zadejte počet kontaktů:"))

for i in range(kont):
    jmeno = input("Zadejte jméno: ")
    cislo = int(input("Zadejte cislo: "))
    seznam[jmeno] = cislo

print(seznam)

klic = input("Koho hledáte??")
print(seznam.get(klic))