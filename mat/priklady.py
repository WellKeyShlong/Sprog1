n = int(input("zadejte cislo: "))
i = 2
prvocislo = True

if 2 > n:
    print (f"cislo {n} je prvocislo")
else:
    while i * i <= n:
        if n % i == 0:
            prvocislo = False
            break
        i += 1

if prvocislo:
    print (f"cislo {n} je prvocislo")
else:
    print (f"cislo {n} neni prvocislo")