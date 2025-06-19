def davp(n, k):
    if n == 1:
        return 0
    else:
        return (davp(n - 1, k) + k) % n

n = 5
k = 3

posledni = davp(n, k)
print(f"{posledni}")