# Program to reverse a number using a while loop

def reverse_number(n):
    reversed_num = 0  # Variable to store the reversed number
    
    while n > 0:
        digit = n % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + digit  # Append the digit to reversed number
        n = n // 10  # Remove the last digit from the original number
    
    return reversed_num

# Taking user input
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"Reversed number: {reversed_num}")

'''
output
Enter a number: 34567
Reversed number: 76543
'''
