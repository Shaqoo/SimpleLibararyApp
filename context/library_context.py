from __future__ import annotations
from typing import List
from entities.book import Book
from entities.user import User

class LibraryContext:
    def __init__(self):
        self.books: List[Book] = []
        self.users: List[User] = []

    

