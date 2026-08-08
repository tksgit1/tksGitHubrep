class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        """
        Borrow a book from the library if available.
        """
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1)  # Decrease the quantity of the borrowed book
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        """
        Return a borrowed book to the library.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_quantity(1)  # Increase the quantity of the returned book
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def view_borrowed_books(self):
        """
        View the list of borrowed books by the user.
        """
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")
