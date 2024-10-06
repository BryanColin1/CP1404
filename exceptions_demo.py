"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
This error happens when the input for either the numerator or the denominator isn't a valid integer,
such as when a user inputs a string that doesn't represent an integer, a float, or any other non-numeric value.

2. When will a ZeroDivisionError occur?
This error is raised when the denominator input by the user is zero.
Since division by zero is undefined, Python flags this as an error.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
To avoid a ZeroDivisionError, we can modify the code by adding a check that ensures the denominator is not zero before
performing the division. If the denominator is zero, we can prompt the user to input a non-zero value or handle it as
an error by raising a ValueError with an appropriate message.
"""

# try:
#    numerator = int(input("Enter the numerator: "))
#    denominator = int(input("Enter the denominator: "))
#    fraction = numerator / denominator
#    print(fraction)
# except ValueError:
#    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#    print("Cannot divide by zero!")
# print("Finished.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")  # Prevent division by zero.
    fraction = numerator / denominator
    print(fraction)
except ValueError as e:
    print(e)  # Handles invalid input and zero denominator.
print("Finished.")
