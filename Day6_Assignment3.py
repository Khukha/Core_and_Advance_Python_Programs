# Python program to find the factorial of a given number using a while loop

def factorial(n):
    # Initialize result to 1 (factorial of 0 and 1 is 1)
    result = 1
    
    # Initialize a counter variable
    i = n
    
    # Use while loop to multiply numbers from n to 1
    while i > 1:
        result *= i  # Multiply result by the current value of i
        i -= 1       # Decrement i by 1
    
    return result  # Return the computed factorial

# Take input from the user
num = int(input("Enter a number: "))

# Check if the input is a non-negative integer
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")

'''
output Enter a number: 8
Factorial of 8 is 40320
'''
