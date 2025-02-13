l = [1,45,8,21,6,3,2,4,5,40,0]

nejv = 0

for i in l:
    if i > nejv:
        nejv = i

print(f"nejvyssi hodnota je {nejv}")

nejm = nejv

for x in l:
    if x < nejm:
        nejm = x

print(f"nejnizsi hodnota je {nejm}")

prum = 0

for f in l:
    prum += f

print(f"prumerna hodnota je {prum / len(l)}")
