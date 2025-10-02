#V1

def bubble1(pole):
    n = len(pole)
    pocet_porovnani = 0

    for i in range(n - 1):
        for j in range(n - 1):
            pocet_porovnani += 1  
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    
    return pocet_porovnani