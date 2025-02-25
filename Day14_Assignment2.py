# Python program to prompt the user for an integer input
# and raise a ValueError if the input is not a valid integer

def get_integer():
    """Function to get a valid integer input from the user."""
    user_input = input("Enter an integer: ")  # Prompt the user for input
    
    # Check if the input is a valid integer
    if not user_input.lstrip('-').isdigit():  # Allow negative numbers
        raise ValueError("Invalid input! Please enter a valid integer.")
    
    return int(user_input)  # Convert and return as integer

# Main program execution
try:
    number = get_integer()  # Attempt to get a valid integer
    print(f"You entered: {number}")  # Print the valid integer
except ValueError as e:
    print(e)  # Print the error message if input is invalid
