#insert

def insert_sort(pole):
    n = len(pole)
    pocet_porovnani = 0

    for i in range(1, n):
        nvm = pole[i]
        j = i - 1

        while j >= 0:
            pocet_porovnani += 1
            if pole[j] > nvm:
                pole[j + 1] = pole[j]
                j -= 1
            else:
                break

        pole[j + 1] = nvm

    return pocet_porovnani


