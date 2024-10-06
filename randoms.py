import random

# Generating a random integer between 5 and 20
print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# The output was a random integer between 5 and 20, inclusive.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20

# Generating a random number from the range 3 to 10, stepping by 2 (i.e., only odd numbers)
print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# The output was a random odd number between 3 and 9.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4?
# No, because the step was 2, starting from 3, so it only produces odd numbers within the given range.

# Generating a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# The output was a random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5

# Code to produce a random number between 1 and 100 inclusive
random_number_between_1_and_100 = random.randint(1, 100)
print(random_number_between_1_and_100)
