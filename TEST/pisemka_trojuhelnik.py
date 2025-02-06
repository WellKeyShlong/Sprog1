#trojuhelnik

#zadani hodnot
a = int(input("Zadejte delku strany a: "))
b = int(input("Zadejte delku strany b: "))
c = int(input("Zadejte delku strany c: "))

#overeni a rozdeleni trojuhelniku
if (a + b) > c and (b + c) > a and (a +c) > b:
    if a == b and b ==c:
        print (f"Strany {a, b, c} tvori rovnostranny trojuhelnik")
    elif a == b or b == c or a == c:
        print (f"Strany {a, b, c} tvori rovnoramenny trojuhelnik")
    else :
        print (f"Strany {a, b, c} tvori obecny trojuhelnik")
else :
    print(f"strany {a, b, c} netvori trojuhelnik")
    