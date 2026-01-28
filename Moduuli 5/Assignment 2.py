luvut = []

while True:
    enter = input("Enter a number: ")
    if enter == "":
        break

    luvut.append(float(enter))
luvut.sort(reverse=True)
print("The greatest numbers in descending order:")
for luku in luvut[:5]:
    print(luku)