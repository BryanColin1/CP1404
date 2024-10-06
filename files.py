# 1: Write the user's name to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as name_file:
    name_file.write(name)

# 2: Read and print the name from the file
with open('name.txt', 'r') as name_file:
    name_from_file = name_file.read().strip()
print(f"Your name is {name_from_file}")

# 3: Read the first two numbers from a file and print their sum
with open('numbers.txt', 'r') as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
print(f"The sum of the first two numbers is: {number1 + number2}")

# 4: Read all numbers from a file and print their total sum
total = 0
with open('numbers.txt', 'r') as numbers_file:
    for line in numbers_file:
        total += int(line)
print(f"The total sum of all numbers is: {total}")