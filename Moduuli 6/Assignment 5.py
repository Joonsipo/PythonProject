def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(number_list)

print(f"Original list: {number_list}")
print(f"List with even numbers only: {filtered_list}")