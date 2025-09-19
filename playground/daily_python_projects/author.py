"""
The program should:
    Define a class Author with attributes:
    name (string)
    birth_year (integer)

Define a class Book with attributes:
    title (string)
    year (integer)
    author (an Author object)

Add the following methods:
    Book.get_info() → returns a string like "Book Title by Author Name"
    Author.write_book(title, year) → returns a new Book instance associated with that author

Bonus (optional):
    Let the author store all books they’ve written
    Add __str__() methods for nicer printing
    Add a method Author.get_bibliography() that prints all titles by the author

This project teaches you how to:
    Build multiple classes that reference each other
    Create object relationships
    Model simple real-world systems like authors and their books
"""
from typing import List, Any

class Author:
    name: str
    birth_year: int
    books: List[Any]

    def __init__(self, name: str, birth_year: int) -> None:
        self.name = name
        self.birth_year = birth_year
        self.books = []

    def __str__(self) -> str:
        return f"{self.name}, {self.birth_year}"
    
    def write_book(self, title: str, year: int) -> Any:
        book = Book(title, year, self)
        self.books.append(book)

        return book
    
    def get_bibliography(self) -> str:
        for book in self.books:
            print(f"- {book.title} ({book.year})")
        return ""


class Book:
    title: str
    year: int
    author: Author

    def __init__(self, title: str, year: int, author: Author) -> None:
        self.title = title
        self.year = year
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author.name}, {self.year}"

    def get_info(self) -> str:
        return f"{self.title} by {self.author}"
    

louis_armstrong = Author("Louis Armstrong", 1901)
etta_james = Author("Etta James", 1936)
chris_cornell = Author("Chris Cornell", 1964)
nina_simone = Author("Nina Simone", 1933)

what_a_wonderful_world = louis_armstrong.write_book("What a Wonderful World", 1967)
la_vie_en_rose = louis_armstrong.write_book("La Vie En Rose", 1950)
at_last = etta_james.write_book("At Last", 1960)
id_rather_go_blind = etta_james.write_book("I'd Rather Go Blind", 1967)
like_a_stone = chris_cornell.write_book("Like a Stone", 2003)
show_me_how_to_live = chris_cornell.write_book("Show Me How to Live", 2005)
feeling_good = nina_simone.write_book("Feeling Good", 1965)
i_put_a_spell_on_you = nina_simone.write_book("I Put a Spell on You", 1965)
revolution = nina_simone.write_book("Revolution", 1968)

print(louis_armstrong.get_bibliography())
print(etta_james.get_bibliography())
print(chris_cornell.get_bibliography())
print(nina_simone.get_bibliography())

print(what_a_wonderful_world.get_info())
print(la_vie_en_rose.get_info())
print(at_last.get_info())
print(id_rather_go_blind.get_info())
print(like_a_stone.get_info())
print(show_me_how_to_live.get_info())
print(feeling_good.get_info())
print(i_put_a_spell_on_you.get_info())
print(revolution.get_info())