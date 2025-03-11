class MovieLibrary:
    # Class attribute: List of all available movies in the library
    available_movies = ['Inception', 'The Matrix', 'The Godfather', 'Pulp Fiction', 'The Shawshank Redemption']

    def __init__(self, member_name):
        # Instance attributes: member name and borrowed movies
        self.member_name = member_name
        self.borrowed_movies = []

    def borrow_movie(self, movie):
        # Borrows a movie if available
        if movie in MovieLibrary.available_movies:
            MovieLibrary.available_movies.remove(movie)
            self.borrowed_movies.append(movie)
            print(f'{movie} has been borrowed by {self.member_name}.')
        else:
            print(f'{movie} is not available in the library.')

    def return_movie(self, movie):
        # Returns a movie to the library
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            print(f'{movie} has been returned by {self.member_name}.')
        else:
            print(f'{movie} is not borrowed by {self.member_name}.')

    def view_borrowed_movies(self):
        # Prints the list of movies borrowed by the member
        if self.borrowed_movies:
            print(f'{self.member_name} has borrowed the following movies:')
            for movie in self.borrowed_movies:
                print(f'- {movie}')
        else:
            print(f'{self.member_name} has not borrowed any movies.')

# Example usage
member1 = MovieLibrary("Alice")

# Borrow movies
member1.borrow_movie("Inception")
member1.borrow_movie("The Matrix")

# View borrowed movies
member1.view_borrowed_movies()

# Return a movie
member1.return_movie("Inception")

# View borrowed movies after returning one
member1.view_borrowed_movies()

# Try to borrow a movie that is unavailable
member1.borrow_movie("The Godfather")
