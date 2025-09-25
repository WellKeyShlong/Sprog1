#V4

def bubble4(pole):
    n = len(pole)
    start = 0
    end = n - 1
    
    while start < end:
        prohodil_se = False

        for i in range(start, end):
            if pole[i] > pole[i + 1]:
                pole[i], pole[i + 1] = pole[i + 1], pole[i]
                prohodil_se = True
        end -= 1  
        
        if not prohodil_se:
            break
            
        for i in range(end, start, -1):
            if pole[i] < pole[i - 1]:
                pole[i], pole[i - 1] = pole[i - 1], pole[i]
                prohodil_se = True
        start += 1 
        
        if not prohodil_se:
            break
    
    return pole