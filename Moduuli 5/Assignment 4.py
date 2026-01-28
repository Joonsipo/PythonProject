kaupungit = []

for n in range(5):
    nimi = input("Enter the name of a city: ")
    kaupungit.append(nimi)

print("\n")
print("The cities you entered: ")

for kaupunki in kaupungit:
    print(kaupunki)