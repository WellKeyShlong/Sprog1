def suda_cisla(zacatek, konec):
    if zacatek > konec:
        return None
    
    for i in range(zacatek, konec + 1):
        if i % 2 == 0:
            print(f"{i}")

suda_cisla(4, 12)

