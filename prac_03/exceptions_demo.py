"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
#Value error occurs when user inputs value of the same data type but an appropriate value
2. When will a ZeroDivisionError occur?
#It occurs when a number is divide by zero because it is not possible to divide any number by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes we can use if statement
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")