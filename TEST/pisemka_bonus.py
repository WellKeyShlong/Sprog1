#trojuhelnik

#zadani hodnot
a = float(input("Zadejte delku strany a: "))
b = float(input("Zadejte delku strany b: "))
c = float(input("Zadejte delku strany c: "))

#overeni a rozdeleni trojuhelniku
if (a + b) > c and (b + c) > a and (a + c) > b:
    if a == b and b ==c:
        print (f"Strany {a, b, c} tvori rovnostranny trojuhelnik")
    elif a == b or b == c or a == c:
        print (f"Strany {a, b, c} tvori rovnoramenny trojuhelnik")
    else :
        print (f"Strany {a, b, c} tvori obecny trojuhelnik")
else :
    print(f"strany {a, b, c} netvori trojuhelnik")

#uhly
if (a ** 2) + (b ** 2) == (c ** 2) or (a ** 2) + (c ** 2) == (b ** 2) or (c ** 2) + (b ** 2) == (a ** 2):
    print ("trojuhelnik je pravouhly")
elif (a ** 2) + (b ** 2) > (c ** 2) and (a ** 2) + (c ** 2) > (b ** 2) and (c ** 2) + (b ** 2) > (a ** 2):
    print ("trojuhelnik je ostrouhly")
else :
    print ("trojuhelnik je tupouhly")