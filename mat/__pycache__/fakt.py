cislo = int(input("zadej cislo more: "))

def faktorial(cislo):
    faktorial = 1
    n = cislo
    nezfaktorialovano = True

    while nezfaktorialovano:
        if n >= 1:
            faktorial *= n
            n -= 1
        else:
            nezfaktorialovano = False
    
    return faktorial

vysledek = (faktorial(cislo))
print (f"faktorial cisla {cislo} je {vysledek}")