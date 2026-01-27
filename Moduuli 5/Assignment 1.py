import random

noppien_heittomaara = int(input("Monta kertaa noppaa heitetään? "))
summa = 0

for n in range(noppien_heittomaara):
    heitto = random.randint(1, 6)
    summa = heitto + 1

print("sum of the dice: ", summa)