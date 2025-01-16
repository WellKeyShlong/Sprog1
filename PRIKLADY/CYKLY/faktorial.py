#zadani hodnot
x = int(input( "Zadejte přirozený základ pro vypočítání faktoriálu: "))
z = x

#vysledek
vysledek = 1
for y in range(x):
    vysledek *=x
    x -=1
print (f"Faktoriál čísla {z} je {vysledek}.")