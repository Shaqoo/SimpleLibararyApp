from __future__ import annotations
from typing import List, Optional
from entities.book import Book
from repositories.interfaces.i_book_repository import IBookRepository
from context.library_context import LibraryContext

class BookRepository(IBookRepository):
    def __init__(self, context: LibraryContext):
        self.context = context

    def add(self, book: Book):
        self.context.books.append(book)

    def get_all(self) -> List[Book]:
        return self.context.books
    
    def get_by_id(self, book_id: int) -> Optional[Book]:
        for book in self.context.books:
            if book.id == book_id:
                return book
        return None