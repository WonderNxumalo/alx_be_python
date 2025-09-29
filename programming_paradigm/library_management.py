class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute to track availability (Encapsulation)
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a user-friendly representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        # Private list to store Book instances (Encapsulation)
        self._books = []

    def add_book(self, title, author):
        """Adds a new Book instance to the library collection."""
        new_book = Book(title, author)
        self._books.append(new_book)
        
    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """Finds a book by title and marks it as available."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """Prints all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(str(book))