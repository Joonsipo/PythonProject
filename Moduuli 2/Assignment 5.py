import math

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = lots * 13.3 + pounds * 32 * 13.3 + talents * 20 * 32 * 13.3
kilograms = int(total_grams // 1000)
remaining_grams = round(total_grams - kilograms * 1000,2)

print(f"The weight in modern units: ")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")