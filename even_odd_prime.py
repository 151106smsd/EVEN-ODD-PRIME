# number_count.py

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Take input as comma-separated numbers
numbers = input("Enter numbers separated by commas: ").split(",")

# Convert to integers
numbers = [int(num) for num in numbers]

even_count = 0
odd_count = 0
prime_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
    if is_prime(num):
        prime_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Prime numbers: {prime_count}")
