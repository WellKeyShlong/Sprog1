
cisla = list(input("Zadej čísla: "))

def insert_sort(pole):
    n = len(pole)
    for i in range(1, n):
        nvm = pole[i]
        j = i - 1
        
        while j >= 0 and pole[j] > nvm:
            pole[j + 1] = pole[j]
            j -= 1
        pole[j + 1] = nvm
    return pole
    
insert_sort(cisla)

print (f"{cisla}")