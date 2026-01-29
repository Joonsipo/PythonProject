import random

N = int(input("Anna satunnaispisteiden määrä: "))
n = 0
i = 0

while i < N:
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1

    if x ** 2 + y ** 2 < 1:
        n = n + 1

    i = i + 1
pi_approx = 4 * n / N
print(f"Approximation of pi: {pi_approx}")