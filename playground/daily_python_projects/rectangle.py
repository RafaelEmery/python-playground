"""
The program should:
    Define a class named Rectangle

The class should have:
    Two instance attributes: width and height (set via the constructor)
    A method area() that returns the area of the rectangle
    A method perimeter() that returns the perimeter of the rectangle
    A method is_square() that returns True if width and height are equal

Bonus (optional):
    Add __str__() to print something like: Rectangle(4 x 5)
    Add input validation to ensure width and height are positive

This project introduces you to writing your own classes — a core concept in building reusable, modular, and real-world Python code.
"""
class Rectangle:
    width: int
    height: int

    def __init__(self, width: int, height: int):
        if width < 0 and height < 0:
            raise Exception("Values must be positive!")
        
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

    def area(self) -> int:
        return self.width * self.height
    
    def perimeter(self) -> int:
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        return self.width == self.height


rect = Rectangle(4, 5)

print(rect)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
print("Is square?", rect.is_square())