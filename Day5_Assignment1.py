
#1Declare a div() function with two parameters.Then call the function and pass two numbers and display their division.
# Function to perform division
def div(a, b):
    """
    This function takes two numbers as input and returns their division.
    If the denominator is zero, it returns an error message.
    """
    # Check if denominator is zero to avoid ZeroDivisionError
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Define two numbers
num1 = 10  # Numerator
num2 = 2   # Denominator

# Calling the function with two numbers and storing the result
result = div(num1, num2)

# Displaying the result
print("The result of division is:", result)

'''
Output The result of division is: 5.0
'''
