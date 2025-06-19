class Book:
    """
    Represents a book in the library.
    """

    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_book_info(self):
        """
        Prints the details of the book.
        """
        print("------ Book Information ------")
        print(f"Title:         {self.title}")
        print(f"Author:        {self.author}")
        print(f"ISBN:          {self.isbn}")
        print(f"Availability:  {self.is_available}")


class LibraryMember:
    """
    Represents a library member.
    """

    def __init__(self, member_id, name) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display_member_info(self):
        """
        Prints the details of the library member.
        """
        print("------ Member Information ------")
        print(f"Member ID:     {self.member_id}")
        print(f"Name:          {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"  - {book.title} (ISBN: {book.isbn})")
        else:
            print("Borrowed Books: No books currently borrowed.")


class Library:
    """
    Represents the library system managing books and members.
    """

    def __init__(self) -> None:
        self.books = {}
        self.members = {}

    def add_book(self, book: Book):
        """
        Adds a book to the library.
        """
        self.books[book.isbn] = book
        print(f"[Added Book] '{book.title}' (ISBN: {book.isbn})")

    def add_member(self, member: LibraryMember):
        """
        Adds a member to the library.
        """
        self.members[member.member_id] = member
        print(f"[Added Member] '{member.name}' (ID: {member.member_id})")

    def borrow_book(self, member_id, isbn):
        """
        Allows a member to borrow a book if available.
        """
        print(f"\n[Borrow Attempt] Member ID: {member_id}, ISBN: {isbn}")

        if member_id not in self.members:
            print("Error: Member not found.")
            return

        if isbn not in self.books:
            print("Error: Book not found.")
            return

        member = self.members[member_id]
        book = self.books[isbn]

        if not book.is_available:
            print(f"Error: Book '{book.title}' is currently unavailable.")
            return

        if book in member.borrowed_books:
            print(f"Error: Book '{book.title}' is already borrowed by this member.")
            return

        book.is_available = False
        member.borrowed_books.append(book)
        print(f"Success: Book '{book.title}' borrowed by {member.name}.")

    def return_book(self, member_id, isbn):
        """
        Allows a member to return a borrowed book.
        """
        print(f"\n[Return Attempt] Member ID: {member_id}, ISBN: {isbn}")

        if member_id not in self.members:
            print("Error: Member not found.")
            return

        if isbn not in self.books:
            print("Error: Book not found.")
            return

        member = self.members[member_id]
        book = self.books[isbn]

        if book not in member.borrowed_books:
            print(f"Error: Book '{book.title}' was not borrowed by {member.name}.")
            return

        book.is_available = True
        member.borrowed_books.remove(book)
        print(f"Success: Book '{book.title}' returned by {member.name}.")

    def list_all_books(self):
        """
        Lists all books in the library.
        """
        print("\n--- All Books in Library ---")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books.values():
                book.display_book_info()

    def list_all_members(self):
        """
        Lists all registered members.
        """
        print("\n--- All Library Members ---")
        if not self.members:
            print("No members registered.")
        else:
            for member in self.members.values():
                member.display_member_info()


library = Library()

# Create Books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "111")
book2 = Book("1984", "George Orwell", "222")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "333")
book4 = Book("The Catcher in the Rye", "J.D. Salinger", "444")

# Add Books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# Create Members
member1 = LibraryMember("M01", "Alice")
member2 = LibraryMember("M02", "Bob")

# Add Members
library.add_member(member1)
library.add_member(member2)

# List All Books and Members
library.list_all_books()
library.list_all_members()

# Borrow Operations
library.borrow_book("M01", "111")
library.borrow_book("M02", "111")
library.borrow_book("M01", "999")
library.borrow_book("X01", "222")
library.borrow_book("M02", "222")

# Return Operations
library.return_book("M01", "111")
library.return_book("M01", "222")
library.return_book("M02", "999")
library.return_book("M03", "222")
library.return_book("M02", "222")

# Final Lists
library.list_all_books()
library.list_all_members()
