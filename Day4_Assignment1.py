  #Python program to check leap year or not

def is_leap_year(year):
    """
    Function to check if a given year is a leap year.
    A year is a leap year if:
    - It is divisible by 4 and not divisible by 100, OR
    - It is divisible by 400.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # Year is a leap year
    else:
        return False  # Year is not a leap year

# Taking input from the user
try:
    year = int(input("Enter a year: "))  # Convert input to integer
    # Check if the year is a leap year using the function
    if is_leap_year(year):
        print(f"{year} is a leap year.")  # Print result if it's a leap year
    else:
        print(f"{year} is not a leap year.")  # Print result if it's not a leap year
except ValueError:
    print("Invalid input! Please enter a valid numerical year.")  # Handle non-numeric input errors



#output: Enter a year: 2024
2024 is a leap year.
 
