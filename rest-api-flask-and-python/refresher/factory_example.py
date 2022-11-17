class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    @classmethod
    def hardcover(cls, name: str, weight: int) -> "Book":
        return cls(name, cls.TYPES[0], weight)

    @classmethod
    def paperback(cls, name: str, weight: int) -> "Book":
        return cls(name, cls.TYPES[1], weight)

    def __repr__(self):
        return f"<Book( '{self.name}, {self.book_type}, weighing {self.weight}g')>"


book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("HOD", 200)
print(book, book2)
