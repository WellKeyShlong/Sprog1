def pocet_cislic(n):
    cislice = 0
    for i in str(abs(n)):
        cislice += 1   
    return cislice

print(pocet_cislic(132465))