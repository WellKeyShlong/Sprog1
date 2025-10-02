#V2

def bubble2(pole):
    n = len(pole)
    pocet_porovnani = 0

    for i in range(n - 1):
        prohodil_se = False
        
        for j in range(n - 1):
            pocet_porovnani += 1  
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
                prohodil_se = True  

        if not prohodil_se:
            break
    
    return pocet_porovnani