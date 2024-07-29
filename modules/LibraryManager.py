# LibraryManager.py


class LibraryManager:
    def __init__(self):
        """Initialize an empty library collection."""
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year, isbn_number):
        """Add a book to the library."""
        if isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[isbn] = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "volume": volume,
            "year": year,
            "isbn": isbn_number,
        }

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
        else:
            raise KeyError("Book with this ISBN does not exist.")

    def get_book_details(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        if isbn in self.books:
            return self.books[isbn]
        else:
            raise KeyError("Book with this ISBN does not exist.")

    def search_books(self, title=None, author=None):
        """Search for books by title or author."""
        results = []
        for book in self.books.values():
            if (title and title.lower() in book["title"].lower()) or (
                author and author.lower() in book["author"].lower()
            ):
                results.append(book)
        return results

    def list_books(self):
        """List all books currently in the library."""
        return list(self.books.values())

    def update_book(
        self,
        isbn,
        title=None,
        author=None,
        publisher=None,
        volume=None,
        year=None,
        isbn_number=None,
    ):
        """Update the details of an existing book."""
        if isbn in self.books:
            book = self.books[isbn]
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if publisher:
                book["publisher"] = publisher
            if volume:
                book["volume"] = volume
            if year:
                book["year"] = year
            if isbn_number:
                book["isbn"] = isbn_number
        else:
            raise KeyError("Book with this ISBN does not exist.")

    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books
