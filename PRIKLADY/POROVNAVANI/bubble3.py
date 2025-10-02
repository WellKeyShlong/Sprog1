#V3

def bubble3(pole):
    n = len(pole)
    pocet_porovnani = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            pocet_porovnani += 1  
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    
    return pocet_porovnani