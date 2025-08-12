# Create list from 1 to 20
numbers = list(range(1, 21))

even_numbers = [n for n in numbers if n % 2 == 0]

even_numbers.reverse()

print("Even numbers in reverse:", even_numbers)
