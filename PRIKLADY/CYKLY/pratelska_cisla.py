#hledani pratelskych cisel
for cislo in range(1, 10000):

    delitel = 0
    delitel2 = 0
    
    for i in range(1, cislo):
        if cislo % i == 0:
            delitel += i
    for i in range(1, delitel):
        if delitel % i == 0:
            delitel2 += i    
    
    if cislo == delitel2:
        print(f"{cislo} - {delitel} jsou pratelska cisla")
