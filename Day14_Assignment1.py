# Python program to handle ZeroDivisionError

def safe_division():
    try:
        # Prompt user for numerator
        numerator = float(input("Enter the numerator: "))
        # Prompt user for denominator
        denominator = float(input("Enter the denominator: "))
        
        # Attempt division
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        # Handle division by zero exception
        print("Error: Cannot divide by zero!")
    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Error: Please enter valid numeric values!")
    finally:
        # This block always executes
        print("Execution completed.")

# Run the function
safe_division()

'''
output
Enter the numerator: 10
Enter the denominator: 2
Result: 5.0
Execution completed.
'''
