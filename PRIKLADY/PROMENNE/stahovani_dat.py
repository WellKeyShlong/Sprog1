
#zadani hodnot
objemDat_MB = int(input("Zadejte objem dat v MB: "))
rchlstSthvni_Mbits = int(input("Zadejte rychlost stahovani v Mbit/s: "))

#vypocet doby stahovani
print(f"Doba stahování je: {round((objemDat_MB * 8) / rchlstSthvni_Mbits, 2)} s")