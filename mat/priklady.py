n = int(input("zadejte cislo: "))

if n <= 2:
    print(f"cislo {n} je prvocislo")

else:
    i = 2
    prvocislo = True

    while i * i <= n:
        if n % i == 0:
            prvocislo = False
            break
        i += 1
        
if prvocislo:
    print(f"cislo {n} je prvocislo")
else: 
    print(f"cislo {n} neni prvocislo")  