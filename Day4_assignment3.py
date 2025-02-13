# Python program to check if a number is positive, negative, or zero

# Input from the user
num = float(input("Enter a number: "))

# Checking if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")  # Output if the number is greater than zero
elif num < 0:
    print("The number is negative.")  # Output if the number is less than zero
else:
    print("The number is zero.")  # Output if the number is exactly zero

#Output
Enter a number: -4
The number is negative
Enter a number: 26
The number is positive.
Enter a number: 0
The number is zero.
