 #Python Program to Find the Largest Among Three Numbers 

def find_largest(num1, num2, num3):
    """
    This function takes three numbers as input and returns the largest among them.
    """
    if num1 >= num2 and num1 >= num3:
        return num1  # num1 is the largest
    elif num2 >= num1 and num2 >= num3:
        return num2  # num2 is the largest
    else:
        return num3  # num3 is the largest

# Taking input from the user
try:
    num1 = float(input("Enter first number: "))  # Convert input to float
    num2 = float(input("Enter second number: "))  # Convert input to float
    num3 = float(input("Enter third number: "))  # Convert input to float

    # Calling function to find the largest number
    largest = find_largest(num1, num2, num3)

    # Printing the largest number
    print(f"The largest number is: {largest}")

except ValueError:
    print("Invalid input! Please enter numeric values.")  # Error handling for non-numeric input


#Output
Enter first number: 34
Enter second number: 21
Enter third number: 67
The largest number is: 67.0
