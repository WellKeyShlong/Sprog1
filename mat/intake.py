vaha_kg = float(input("Zadejte vasi vahu (kg): "))
vaha = vaha_kg / 0.45

kalorie = vaha * 12
tuk = kalorie / 36
protein = vaha * 0.8
sach = ((kalorie - (protein * 4))-(tuk *9)) / 4
vlaknina = (kalorie/1000)*14

print (f"Vas idealni prijem Kalorii denne je: {round(kalorie)},")
print (f"idealni prijem tuku denne je: {round(tuk)}g,")
print (f"idealni prijem proteinu denne je: {round(protein)}g,")
print (f"idealni prijem sacharidu denne je: {round(sach)},")
print (f"idealni prijem vlakniny denne je: {round(vlaknina)}g")