import random
hranice = int(input("Zadej hranici: "))
cisla = [random.randint(1,100) for i in range(hranice)]

def bubble(cisla):
    nesetrizeno = True

    while nesetrizeno:
        nesetrizeno = False
        for i in range(len(cisla) - 1):
                if cisla[i] > cisla[i + 1]:
                    cisla[i], cisla[i + 1] = cisla[i + 1], cisla[i]
                    nesetrizeno = True
    
    return cisla

print(f"nesetrizeny seznam: {cisla}")
print(f"nesetrizeny seznam: {bubble(cisla)}")