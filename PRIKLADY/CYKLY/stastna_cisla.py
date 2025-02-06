pocet = 0

def soucet_cifer(n):
    soucet = 0
    while n > 0:
        cifra = n % 10
        soucet += cifra ** 2
        n = n // 10
    return soucet

def stastne_cislo(n):
    navstivene = set()
    while n != 1 and n not in navstivene:
        navstivene.add(n)
        n = soucet_cifer(n)
    return n == 1

def najdi_stastna_cisla(max_cislo):
    stastna_cisla = []
    for i in range(1, max_cislo + 1):
        if stastne_cislo(i):
            stastna_cisla.append(i)
            global pocet 
            pocet += 1
    return stastna_cisla


stastna_cisla = najdi_stastna_cisla(10000)
print(stastna_cisla)

pravd = pocet / 100
print(pravd)