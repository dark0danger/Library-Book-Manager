from dataclasses import dataclass


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    year: int
    is_borrowed: bool = False
