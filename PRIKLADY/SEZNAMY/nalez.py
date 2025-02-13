l = [2,3,1,0,5,6,4,2]

nalez = int(input("Zadejte cislo, ktere chcete najit: "))

pozic = 0
for i in l:
    if i == nalez:
        print(f"index je {pozic}")
    pozic += i