from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.book import Book

class IBookService(ABC):

    @abstractmethod
    def add_book(self, title, author, date_published):
        pass

    @abstractmethod
    def borrow_book(self, book_id, user_id):
        pass

    @abstractmethod
    def return_book(self, book_id, email):
        pass

    @abstractmethod
    def get_by_id(self, book_id) -> Optional[Book]:
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass