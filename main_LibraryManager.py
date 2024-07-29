# main.py

from modules.LibraryManager import LibraryManager

# Initialize LibraryManager
library = LibraryManager()

# Add some sample books
library.add_book(
    "978-1234567890",
    "Introduction to Operating Systems",
    "John Doe",
    "Tech Press",
    "1st",
    2021,
    "978-1234567890",
)
library.add_book(
    "978-0987654321",
    "Data Structures in Python",
    "Jane Smith",
    "Code Press",
    "2nd",
    2023,
    "978-0987654321",
)
library.add_book(
    "978-1122334455",
    "Machine Learning with Python",
    "Alice Johnson",
    "AI Press",
    "1st",
    2022,
    "978-1122334455",
)

# List all books
print("All Books in Library:")
for book in library.list_books():
    print(book)

# Retrieve and display the details of a book
isbn_to_check = "978-1234567890"
print("\nDetails of book with ISBN", isbn_to_check, ":")
print(library.get_book_details(isbn_to_check))

# Search for books by title
print("\nSearch results for title 'Python':")
for book in library.search_books(title="Python"):
    print(book)

# Update a book's details
library.update_book("978-1234567890", title="Advanced Operating Systems")

# Check availability
isbn_to_check = "978-1234567890"
print("\nIs book with ISBN", isbn_to_check, "available?")
print(library.check_availability(isbn_to_check))

# Remove a book
library.remove_book("978-1234567890")

# Check availability again
print("\nIs book with ISBN", isbn_to_check, "available after removal?")
print(library.check_availability(isbn_to_check))

# List all books after removal
print("\nAll Books in Library after removal:")
for book in library.list_books():
    print(book)
