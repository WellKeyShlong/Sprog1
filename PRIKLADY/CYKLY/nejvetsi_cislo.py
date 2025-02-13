
#zadani hodnot
cislo1 = int(input ("Zadejte první číslo: "))
cislo2 = int(input ("Zadejte druhé číslo: "))
cislo3 = int(input ("Zadejte třetí číslo: "))

#zjisteni nejvetsiho cisla
if cislo1 > cislo2 and cislo1 >  cislo3:
    print (f"Největší číslo je {cislo1}")
elif cislo2 > cislo1 and cislo2 > cislo3:
    print (f"Největší číslo je {cislo2}")
else:
    print (f"Největší číslo je {cislo3}")