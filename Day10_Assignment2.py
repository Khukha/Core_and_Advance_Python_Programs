# Function to find the largest and smallest number in a list
def find_min_max(lst):
    # Check if the list is empty
    if not lst:
        return None, None  # Return None for both if list is empty
    
    # Initialize min and max with the first element of the list
    smallest = lst[0]
    largest = lst[0]
    
    # Iterate through the list to find min and max
    for num in lst:
        if num < smallest:
            smallest = num  # Update smallest if a smaller number is found
        if num > largest:
            largest = num  # Update largest if a larger number is found
    
    return smallest, largest  # Return the results

# Example usage
numbers = [3, 1, 8, 5, 2, 10, -1, 6]
smallest, largest = find_min_max(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
