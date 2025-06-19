def nsd(a, b):
    if b == 0:
        return a
    else:
        return nsd (b, a % b)
    
print (nsd (105, 252))