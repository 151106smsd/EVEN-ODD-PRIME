# number_count.py

# Take input as comma-separated numbers
numbers = input("Enter numbers separated by commas: ").split(",")

# Convert to integers
numbers = [int(num) for num in numbers]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
