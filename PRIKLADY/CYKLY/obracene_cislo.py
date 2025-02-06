# Funkce pro převrácení čísla
def prevratit_cislo(cislo):
    # Proměnná pro uložení převráceného čísla
    prevracene_cislo = 0
    
    # Zajistíme, že číslo je kladné, pokud je záporné, uložíme si informaci o znaménku
    znameni = 1 if cislo >= 0 else -1
    cislo = abs(cislo)
    
    # Provádíme převracení čísla
    while cislo > 0:
        # Získáme poslední číslici
        posledni_cislice = cislo % 10
        prevracene_cislo = prevracene_cislo * 10 + posledni_cislice
        cislo //= 10
    
    # Vracení výsledku s původním znaménkem
    return prevracene_cislo * znameni

# Získání čísla od uživatele
cislo = int(input("Zadejte číslo: "))

# vypsání výsledku
prevracene_cislo = prevratit_cislo(cislo)
print(f"Převrácené číslo je: {prevracene_cislo}")