nalada = int(input("jak se mas? Odpovez 0-10: "))

def naladometr(nalada):
    if nalada == 0:
        print ("sracko nedelej")
    elif nalada == 1:
        print ("muze byt hur")
    elif nalada == 2:
        jakto = input("jaj, jakto? ")
        print (f"sry ale na {jakto} ti fakt neodpovim, nechce se mi vymyslet tolik odpovedi na vsechny duvody proc ses ufnukana devka")
    elif nalada == 3:
        print("damn, to je blby")
    elif nalada == 4:
        print("a tak muze to byt horsi (sry nejsem moc empatickej)")
    elif nalada == 5:
        print("to neni tak hrozny ne? doslova prumer proste")
    elif nalada == 6:
        print("to je chill, asi, idk")
    elif nalada == 7:
        jone = input("okej to je pohoda ne? ")
        if jone == "ne":
            print("si naser")
        else:
            print("at si rekl cokoliv tak si naser, nechce se mi to programovat")
    elif nalada == 8:
        print("okej to je hodne pohodicka")
    elif nalada == 9:
        print("dobry nechci slyset o tom jak sis zasukal")
    elif nalada == 10:
        print("neverim")
    else:
        print("didopice")
     

print(naladometr(nalada))