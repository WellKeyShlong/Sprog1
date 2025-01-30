# Zadání čísla jako string pro zajištění, že zpracujeme všechny cifry
cislo = input("Zadejte víceciferné číslo: ")

# Inicializace proměnných pro nejvyšší a nejnižší cifru
max = max(cislo)
min = min(cislo)

# Výpis výsledků
print(f"Nejvyšší cifra: {max}")
print(f"Nejnižší cifra: {min}")