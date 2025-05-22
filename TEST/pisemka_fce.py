import random

def prehazet(slovo):
    prehazene = []

    for i in slovo:
        delka = len(prehazene)
        rnd = random.randint(0,delka)
        prehazene.insert(rnd, i)
    
    prehazene_slovo = "".join(prehazene)

    return prehazene_slovo

print(prehazet("Ahoj"))
