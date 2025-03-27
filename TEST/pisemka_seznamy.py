#spojeni seznamu

#zadani delek
del1 = int(input("Zadejte délku prvního seznamu: "))
del2 = int(input("Zadejte délku druhého seznamu: "))

#prvni seznam
sezn1 = []
for i in range (del1):
    sezn1.append(int(input(f"Zadejte {i + 1}. číslo prvního seznamu: ")))

#druhy seznam
sezn2 = []
for i in range (del2):
    sezn2.append(int(input(f"Zadejte {i + 1}. číslo druhého seznamu: ")))

#slouceni seznamu
sloucSezn = []
delkmax = max(del1, del2)
for i in range(delkmax):
        if i < del1:
            sloucSezn.append(sezn1[i])
        if i < del2:
            sloucSezn.append(sezn2[i])
print (f"{sloucSezn}")