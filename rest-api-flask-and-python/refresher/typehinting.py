from typing import List


def list_avg(seq: List) -> float:
    return sum(seq) / len(seq)


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books
    
    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books"