from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional
from entities.book import Book

class IBookRepository(ABC):
    @abstractmethod
    def add(self, book: Book):
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        pass