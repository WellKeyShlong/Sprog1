delka = int(input("zadejte horni mez: "))

cisla = [True] = delka

cisla[0] = False
cisla[1] = False

for i in range(2, delka):
    for j in range(i*2,delka,i):
        cisla[j] = False

for i in range(delka):
    if cisla[i]:
        print (i)


cisla_2 = [x for x in range(delka)]

print(cisla_2)
cisla_2.remove(0)
cisla_2.remove(1)
print(cisla_2)
for cislo in cisla_2:
    for i in range(int(cisla_2[-1]/cislo+1)):
        nasobek = cislo*i
        if nasobek in cisla_2:
            cisla_2.remove(nasobek)

print(cisla_2)