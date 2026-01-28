import random

noppien_heittomaara = int(input("How many dice to roll: "))
summa = 0

for _ in range(noppien_heittomaara):
    heitto = random.randint(1, 6)
    summa = heitto + summa

print(f"Sum of the dice: {summa}")