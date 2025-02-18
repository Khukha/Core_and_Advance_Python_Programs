# Python program to sum all the items in a list

def sum_list(numbers):
    """
    This function takes a list of numbers as input
    and returns the sum of all the numbers in the list.
    """
    total = 0  # Initialize total sum to 0
    
    for num in numbers:  # Iterate through each number in the list
        total += num  # Add the number to total sum
    
    return total  # Return the final sum

# Example usage
numbers = [1, 2, 3, 4, 5]  # Define a list of numbers
result = sum_list(numbers)  # Call the function with the list
print("Sum of all items in the list:", result)  # Print the result
