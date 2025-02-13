soucmoc = 0
mocn = 0

for i in range(0, 101):
    soucmoc += i ** 2

for x in range(0, 101):
    mocn += x

mocn = mocn ** 2

print (f"rozdíl mezi součtem druhých mocnin prvních sta přirozených čísel a druhou mocninou tohoto součtu je {mocn - soucmoc}")