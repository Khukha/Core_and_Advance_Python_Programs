class Library:
    # Class attributes
    total_books = 0
    all_books = []

    def __init__(self):
        self.members = []

    @classmethod
    def view_library_books(cls):
        print(f"Total books available: {cls.total_books}")
        print("List of available books:")
        for book in cls.all_books:
            print(book)

    def add_member(self, member_name):
        member = LibraryMember(member_name)
        self.members.append(member)

    def add_book(self, book):
        Library.all_books.append(book)
        Library.total_books += 1


class LibraryMember:
    # Instance attributes
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        # Check if the book is available
        if book in Library.all_books:
            # Add to the member's borrowed_books list
            self.borrowed_books.append(book)
            # Remove from the library's all_books list
            Library.all_books.remove(book)
            # Decrease the total books count
            Library.total_books -= 1
            print(f"{self.name} has borrowed the book: {book}")
        else:
            print(f"Book '{book}' is not available.")

    def return_book(self, book):
        # Check if the member has borrowed the book
        if book in self.borrowed_books:
            # Add the book back to the library's list
            Library.all_books.append(book)
            # Remove from the borrowed_books list
            self.borrowed_books.remove(book)
            # Increase the total books count
            Library.total_books += 1
            print(f"{self.name} has returned the book: {book}")
        else:
            print(f"{self.name} has not borrowed the book: {book}")


# Testing the program
library = Library()

# Adding books to the library
library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")
library.add_book("Moby Dick")

# Viewing available books
Library.view_library_books()

# Adding library members
library.add_member("Alice")
library.add_member("Bob")

# Borrowing and returning books
alice = library.members[0]
bob = library.members[1]

alice.borrow_book("1984")
bob.borrow_book("Moby Dick")

# Viewing available books after borrowing
Library.view_library_books()

# Returning books
alice.return_book("1984")
bob.return_book("Moby Dick")

# Viewing available books after returning
Library.view_library_books()
