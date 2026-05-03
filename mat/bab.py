import random

lenght =  int(input("zadejte delku seznamu: "))
cisla = [random.randint(1, 100) for i in range(lenght)]

def bubble(cisla):
    neserazeno = True
    
    while neserazeno:
        neserazeno =  False
        for i in range(len(cisla) - 1):
            if cisla[i] > cisla[i + 1]:
                cisla[i], cisla[i + 1] = cisla[i + 1], cisla[i]
                neserazeno = True
    return cisla
            
print (f"neserazeny seznam {cisla}")
print (f"serazeny seznam {bubble(cisla)}")