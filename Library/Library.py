class Library:
    def __init__(self):
        self.books = []  # List to store all books in the library
        self.users = []  # List to store all users of the library

    def add_book(self, book):
        """
        Add a book to the library.
        """
        self.books.append(book)

    def register_user(self, user):
        """
        Register a new user in the library if the user ID doesn't already exist.
        """
        if any(curr_user.user_id == user.user_id for curr_user in self.users):
            print("User with the same ID already exists! Try another ID.")
            return
        self.users.append(user)
        print(f"New user {user.name} added successfully!")

    def search_book_by_title(self, title):
        """
        Search for books by title.
        """
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def list_books(self):
        """
        List all books in the library.
        """
        if self.books:
            print("Books in the Library:")
            for book in self.books:
                book.display_book_info()
        else:
            print("No books available in the library.")

    def add_new_book(self):
        """
        Add a new book to the library with user input.
        """
        book_id = int(input("Enter book ID: "))
        if any(book.book_id == book_id for book in self.books):
            print("Book with the same ID already exists, please try another ID.")
            return

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        quantity = int(input("Enter the quantity of books: "))

        new_book = Book(book_id, title, author, quantity)
        self.add_book(new_book)
        print("Book added successfully!")
        new_book.display_book_info()
