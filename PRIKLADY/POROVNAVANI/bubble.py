import time

cisla = list(input("Zadej čísla: "))

#V1

def bubble(pole):
    n = len(pole)
    pocet_por1 = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            pocet_por1 += 1
            if pole[j] > pole[j + 1]:
                pole[j], pole[j +1] = pole[j +1], pole[j]
    return  pocet_por1

print (f"Puvodní čísla: {cisla}")

def measure_sort():
    time_start = time.perf_counter()
    serazena = bubble(cisla)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"bubble v1 - porovnani: {serazena}, cas: {execution_time}")

measure_sort()

#V2

def bubble2(pole):
    n = len(pole)
    pocet_por2 = 0

    for i in range(n):
        setrizene = False

        for j in range(0, n - i - 1):
            pocet_por2 +=1
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
                setrizene = True
    
        if not setrizene:
            break

    return pocet_por2

def measure_sort2():
    time_start = time.perf_counter()
    serazena2 = bubble2(cisla)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"bubble v2 - porovnani: {serazena2}, cas: {execution_time}")

measure_sort2()

#V3

def bubble3(pole):
    n = len(pole)
    pocet_por3 = 0

    start = 0
    konec = n - 1
    setrizene = True

    while setrizene:
        setrizene = False

        for i in range(start, konec):
            pocet_por3 += 1
            if pole[i] > pole[i + 1]:
                pole[i], pole[i + 1] = pole[i + 1], pole[i]
                setrizene = True

        if not setrizene:
            break

        konec -= 1
        setrizene = False

        for i in range(konec, start, -1):
            pocet_por3 += 1
            if pole[i - 1] > pole[i]:
                pole[i], pole[i - 1] = pole[i - 1], pole[i]
                setrizene = True

        start += 1

    return pocet_por3


def measure_sort3():
    time_start = time.perf_counter()
    serazena3 = bubble3(cisla)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"bubble v3 - porovnani: {serazena3}, cas: {execution_time}")

measure_sort3()