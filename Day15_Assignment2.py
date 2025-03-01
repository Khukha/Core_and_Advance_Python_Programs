# Here’s a Python function that counts and displays the total number of words in a text file named "ABC.txt"
# Function to create the "ABC.txt" file with some sample content
def create_file():
    content = "Hello Guys How are you"
    
    with open("ABC.txt", "w") as file:
        file.write(content)

# Function to count the total number of words in "ABC.txt"
def count_words():
    try:
        word_count = 0
        with open("ABC.txt", "r") as file:
            for line in file:
                words = line.split()  # Split the line into words
                word_count += len(words)

        print(f"Total number of words in 'ABC.txt': {word_count}")
    except FileNotFoundError:
        print("The file 'ABC.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# First, create the file with content
create_file()

# Now, count and display the number of words in the file
count_words()

'''     OUTPUT
Total number of words in 'ABC.txt': 5
'''
