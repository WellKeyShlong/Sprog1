import random

random_digits = ''.join(str(random.randint(0, 9)) for _ in range(1_000_000))

print(f"{random_digits}")