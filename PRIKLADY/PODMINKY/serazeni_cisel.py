
#zadani hodnot
cislo1 = int(input ("Zadejte první číslo: "))
cislo2 = int(input ("Zadejte druhé číslo: "))
cislo3 = int(input ("Zadejte třetí číslo: "))

#nalezeni nejvetsiho cisla
if cislo1 > cislo2 and cislo1 > cislo3:
    nejCislo = cislo1
elif cislo2 > cislo1 and cislo2 > cislo3:
    nejCislo = cislo2
else:
    nejCislo = cislo3

#nalezeni prostredniho cisla
if cislo1 > cislo2 and cislo3 > cislo1 or cislo1 < cislo2 and cislo3 < cislo1:
    midCislo = cislo1
elif cislo2 > cislo1 and cislo3 > cislo2 or cislo2 < cislo3 and cislo1 < cislo2:
    midCislo = cislo2
else:
    midCislo = cislo3

#nalezeni nejmensiho cisla
if cislo1 < cislo2 and cislo1 < cislo3:
    nejmCislo = cislo1
elif cislo2 < cislo1 and cislo2 < cislo3:
    nejmCislo = cislo2
else:
    nejmCislo = cislo3

#vypsání
if cislo1 == nejCislo and cislo2 == midCislo and cislo3 == nejmCislo:
    print (f"Čísla jsou v sestupném pořadí: {cislo1}; {cislo2}; {cislo3}")
elif cislo1 == nejCislo and cislo3 == midCislo and cislo2 == nejmCislo:
    print (f"Čísla jsou v sestupném pořadí: {cislo1}; {cislo3}; {cislo2}")
elif cislo2 == nejCislo and cislo1 == midCislo and cislo3 == nejmCislo:
    print (f"Čísla jsou v sestupném pořadí: {cislo2}; {cislo1}; {cislo3}")
elif cislo2 == nejCislo and cislo3 == midCislo and cislo1 == nejmCislo:
    print (f"Čísla jsou v sestupném pořadí: {cislo2}; {cislo3}; {cislo1}")
elif cislo3 == nejCislo and cislo2 == midCislo and cislo1 == nejmCislo:
    print (f"Čísla jsou v sestupném pořadí: {cislo3}; {cislo2}; {cislo1}")
else:
    print (f"Čísla jsou v sestupném pořadí: {cislo3}; {cislo1}; {cislo2}")