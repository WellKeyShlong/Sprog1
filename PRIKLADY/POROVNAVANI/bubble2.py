#V2

def bubble2(pole):
    n = len(pole)
    
    for i in range(n - 1):
        prohodil_se = False
        
        for j in range(n - 1):
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
                prohodil_se = True  

        if not prohodil_se:
            print(f"Pole seřazeno po {i + 1} průchoduech")
            break
    
    return pole