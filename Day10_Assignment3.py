# Python program to find duplicate values in a list

def find_duplicates(lst):
    """
    Function to find and display duplicate values in a list.
    :param lst: List of elements
    :return: List of duplicate elements
    """
    element_count = {}  # Dictionary to store the count of each element
    duplicates = []  # List to store duplicate values

    # Iterate through the list and count occurrences of each element
    for item in lst:
        if item in element_count:
            element_count[item] += 1  # Increment count if element is already in dictionary
        else:
            element_count[item] = 1  # Initialize count for new element
    
    # Identify elements that appear more than once
    for key, value in element_count.items():
        if value > 1:
            duplicates.append(key)
    
    return duplicates

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 7, 9, 13, 3]
    duplicates = find_duplicates(sample_list)
    print("Duplicate values:", duplicates)

 '''
#Output
Duplicate values: [2, 3, 7]
'''
