from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book("Brave New World", "Aldous Huxley")
    library.add_book("1984", "George Orwell")

    # Initial list of available books (Expected: Both books)
    print("Available books after setup:")
    library.list_available_books()
    print("-" * 20) # Separator for clear output

    # Simulate checking out a book '1984'
    library.check_out_book("1984")
    # List available books (Expected: Only Brave New World)
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()
    print("-" * 20)

    # Simulate returning a book '1984'
    library.return_book("1984")
    # List available books (Expected: Both books again)
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
    
if __name__ == "__main__":
    main()