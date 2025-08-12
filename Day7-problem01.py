# Lists and List methods
num = []

for i in range(1, 6):
    numbers = float(input(f"Enter a Number in Decimal form ({i}): "))
    num.append(numbers)

print(f"All numbers in list: {num}")
print("Maximum number:", max(num))
print("Minimum number:", min(num))
print("Sum of all numbers:", sum(num))
