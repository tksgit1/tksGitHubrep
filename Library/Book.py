class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity  # Available quantity of the book

    def display_book_info(self):
        """
        Display the book's details (ID, Title, Author, Quantity).
        """
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available Quantity: {self.quantity}")

    def check_availability(self):
        """
        Check if the book is available (quantity > 0).
        """
        return self.quantity > 0

    def update_quantity(self, quantity):
        """
        Update the quantity of the book (borrow or return).
        """
        self.quantity += quantity
