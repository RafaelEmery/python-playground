"""
Create two classes.

Book class that:
    Stores title, author, ISBN, and availability status
    Has methods to check out and return the book
    Displays book information

Library class that:
    Manages a collection of books
    Can add and remove books
    Search for books by title or author
    Display available books
    Track checked out books

Bonus (optional):
    Add due dates for checked out books
    Create a Member class for library users
    Add book categories/genres
    Generate library reports

This project gives you: 
    Hands-on practice with multiple classes
    Object relationships, and data management
"""
from datetime import datetime, timedelta
from typing import List

class Member:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


class Genre:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Category:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Book:
    title: str
    author: str
    isbn_number: int
    available: bool
    due_date: datetime
    booked_by: Member
    genre: Genre
    category: Category

    def __init__(
        self, 
        title: str, 
        author: str, 
        isbn_number: int,
        genre_name: str,
        category_name: str
    ) -> None:
        self.title = title
        self.author = author
        self.isbn_number = isbn_number
        self.available = True
        self.due_date = None
        self.booked_by = None
        self.genre = Genre(genre_name)
        self.category = Category(category_name)

    def __str__(self) -> str:
        return f"{self.title} by {self.author} | {self.genre} - {self.category}"

    def update_category(self, name: str) -> None:
        self.category = Category(name)

    def book(self, requester_name: str) -> str:
        if self.available:
            self.available = False
            self.due_date = datetime.now() + timedelta(weeks=1)
            self.booked_by = Member(requester_name)

            return f"{self.title} successfully booked | Must be returned at {self.due_date}"
        else: 
            return f"{self.title} already booked by {self.booked_by} | Will be available at {self.due_date}"
        
    def give_back(self) -> str:
        self.available = True
        self.due_date = None
        self.booked_by = None

        return f"{self.title} is now available =)"


class Library:
    name: str
    address: str
    books: List[Book]

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.books = []

    def __str__(self) -> str:
        return f"{self.name} at {self.address}"
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)


best_library_ever = Library("Blue Note Library", "Rua do Jazz, 123")

whats_going_on = Book(
    title="What's Going On", 
    author="Marvin Gaye", 
    isbn_number=12345,
    genre_name="Soul",
    category_name="Biography"
)
feeling_good = Book(
    title="Feeling Good", 
    author="Nina Simone", 
    isbn_number=67890,
    genre_name="Jazz",
    category_name="Autobiography"
)
my_way = Book(
    title="My Way", 
    author="Frank Sinatra", 
    isbn_number=11111,
    genre_name="Pop",
    category_name="Memoirs"
)
purple_rain = Book(
    title="Purple Rain", 
    author="Prince", 
    isbn_number=22222,
    genre_name="Funk",
    category_name="Biography"
)

best_library_ever.add_book(whats_going_on)
best_library_ever.add_book(feeling_good)
best_library_ever.add_book(my_way)
best_library_ever.add_book(purple_rain)

print(whats_going_on.book("Stevie Wonder"))
print(feeling_good.book("Aretha Franklin"))
print(my_way.book("Ella Fitzgerald"))

print(whats_going_on.book("John Coltrane"))

print(whats_going_on.give_back())
print(feeling_good.give_back())

print(whats_going_on.book("Miles Davis"))
print(purple_rain.book("Billie Holiday"))

print(f"Before: {my_way}")
my_way.update_category("Classic Memoirs")
print(f"After: {my_way}")

best_library_ever.remove_book(purple_rain)
print(f"Remaining books: {len(best_library_ever.books)}")