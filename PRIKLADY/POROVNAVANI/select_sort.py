#select

def select_sort(pole):
    n = len(pole)
    pocet_porovnani = 0

    for i in range(n):
        min = i

        for j in range(i + 1, n):
            pocet_porovnani += 1
            if pole[j] < pole[min]:
                min = j

        pole[i], pole[min] = pole[min], pole[i]
    
    return pocet_porovnani