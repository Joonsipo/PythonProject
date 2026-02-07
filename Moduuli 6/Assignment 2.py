import random

def roll_dice(sides):
    return random.randint(1, sides)

max_sides = int(input("Anna nopan tahkojen määrä: "))

while True:
    result = roll_dice(max_sides)
    print(result)
    if result == max_sides:
        break