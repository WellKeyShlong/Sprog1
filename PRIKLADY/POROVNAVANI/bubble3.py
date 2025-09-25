#V3

def bubble3(pole):
    n = len(pole)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    
    return pole