#vstupy
celsius = int(input("Zadejte teplotu ve stupních Celsia: "))

#výpočty
kelviny = round(celsius + 273.15, 2)
farenheity = round(celsius * (9/5) + 32, 2)

print(f"Hodnota v Kelvinech je: {kelviny} a hodnota ve Farenheitech je: {farenheity})")
      