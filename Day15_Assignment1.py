# Python function that reads the content of a text file named "ABC.txt" line by line and displays the content on the screen
def read_file():
    try:
        with open("ABC.txt", "r") as file:
            for line in file:
                print(line, end='')  # 'end' is used to avoid adding extra newline
    except FileNotFoundError:
        print("The file 'ABC.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to read and display the content
read_file()


'''     OUTPUT
Hello Guys How are you
'''
