numbers = []
while True:
    enter = input("Enter a number (or press Enter to quit): ")
    if enter == "":
        break
    numbers.append(float(enter))
if numbers:
    if numbers:
        print("Smallest number:", min(numbers))
        print("Largest number:", max(numbers))
else:
    print("number was not entered.")