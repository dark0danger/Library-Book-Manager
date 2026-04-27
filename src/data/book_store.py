from typing import List

from models.book import Book


class BookStore:
    def __init__(self) -> None:
        self._books: List[Book] = []
        self._next_id = 1
        self._seed_data()

    def _seed_data(self) -> None:
        self.add_book("Clean Code", "Robert C. Martin", 2008)
        self.add_book("The Pragmatic Programmer", "Andrew Hunt", 1999)
        self.add_book("Design Patterns", "Erich Gamma", 1994)

    def add_book(self, title: str, author: str, year: int) -> Book:
        book = Book(
            book_id=self._next_id,
            title=title.strip(),
            author=author.strip(),
            year=year,
        )
        self._books.append(book)
        self._next_id += 1
        return book

    def get_all_books(self) -> List[Book]:
        return list(self._books)

    def search_books(self, keyword: str) -> List[Book]:
        normalized = keyword.strip().lower()
        if not normalized:
            return self.get_all_books()
        return [
            b
            for b in self._books
            if normalized in b.title.lower() or normalized in b.author.lower()
        ]

    def borrow_book(self, book_id: int) -> bool:
        book = self.get_book_by_id(book_id)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False

    def return_book(self, book_id: int) -> bool:
        book = self.get_book_by_id(book_id)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return True
        return False

    def delete_book(self, book_id: int) -> bool:
        for index, book in enumerate(self._books):
            if book.book_id == book_id:
                del self._books[index]
                return True
        return False

    def get_book_by_id(self, book_id: int) -> Book | None:
        for book in self._books:
            if book.book_id == book_id:
                return book
        return None

    def get_stats(self) -> dict[str, int]:
        total = len(self._books)
        borrowed = sum(1 for b in self._books if b.is_borrowed)
        available = total - borrowed
        return {
            "total": total,
            "borrowed": borrowed,
            "available": available,
        }
