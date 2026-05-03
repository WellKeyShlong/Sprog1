import random

moznosti = ["kamen", "nuzky", "papir"]
pokracovat = True
s_j= 0 
s_p= 0

while pokracovat:
    moje = int(input("0 = kamen, 1 = nuzky, 2 = papir: "))
    pocitac = random.randint(0, 2)

    if moje > 2 or moje < 0:
        print ("hraj podle pravidel demente")
    elif moje == pocitac:
        print("Pocitac zvolil:", moznosti[pocitac])
        print("Remiza")
    elif (moje==2 and pocitac==0 or moje==1 and pocitac==2 or moje==0 and pocitac==1):
        print("Pocitac zvolil:", moznosti[pocitac])
        print("Vyhral jste")
        s_j += 1
    else:
        print("Pocitac zvolil:", moznosti[pocitac])
        print("Pocitac vyhral")
        s_p += 1
    
    print (f"skore: pc = {s_p}, vase = {s_j}")
    znovu = input("Chcete hrát znovu? a/n:")
    if znovu == "n":
        pokracovat = False
    if znovu not in("n", "a"):
        print ("pico nech toho")
