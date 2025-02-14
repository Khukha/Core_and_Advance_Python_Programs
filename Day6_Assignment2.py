 #Function to check if a number is palindrome
def is_palindrome(num):
    # Convert number to string
    str_num = str(num)
    
    # Reverse the string and compare with original
    if str_num == str_num[::-1]:
        return True
    else:
        return False

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is palindrome and print result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
 print(f"{num} is not a palindrome.")


'''
output Enter a number: 121
121 is a palindrome.
'''
