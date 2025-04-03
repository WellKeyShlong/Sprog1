def prevod_na_minuty(hodiny, minuty):
    if hodiny < 0 or minuty < 0:
        return None
    else: 
        print(f"{hodiny * 60 + minuty}")

prevod_na_minuty(5, 40)