luku = int(input("Enter an integer: "))

if luku < 2:
    print(f"{luku} is not a prime number.")
else:
    alkuluku = True
    for n in range(2, int(luku ** 0.5) + 1):
        if luku % n == 0:
            alkuluku = False
            break

    if alkuluku:
        print(f"{luku} is a prime number.")
    else:
        print(f"{luku} is not a prime number.")