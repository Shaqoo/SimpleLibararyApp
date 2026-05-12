from __future__ import annotations
from services.interfaces.i_book_service import IBookService
from repositories.interfaces.i_book_repository import IBookRepository
from repositories.interfaces.i_user_repository import IUserRepository
from entities.book import Book
from utils.validators import Validator  
from colorama import Fore
from typing import Optional, List

class BookService(IBookService):
    def __init__(self, book_repository: IBookRepository, user_repository: IUserRepository):
        self.book_repository = book_repository
        self.user_repository = user_repository

    def add_book(self, title: str, author: str, date_published: str) -> None:
        if not Validator.is_not_empty(title) or not Validator.is_not_empty(author):
            print(Fore.RED + "Error: Title and Author cannot be empty.")
            return

        books = self.book_repository.get_all()
        book_id = max([b.id for b in books], default=0) + 1
        
        book = Book(book_id, title, author, date_published)
        self.book_repository.add(book)
        print(Fore.GREEN + f"Book '{title}' added successfully with ID {book_id}.")

    def borrow_book(self, book_id: int, user_id: int) -> None:
        book = self.book_repository.get_by_id(book_id)
        user = self.user_repository.get_by_id(user_id)

        if not book:
            print(Fore.RED + "Error: Book ID does not exist.")
            return
        if not user:
            print(Fore.RED + "Error: User not found.")
            return

        if book.is_borrowed:
            print(Fore.YELLOW + f"Notice: '{book.title}' is already borrowed by {book.borrowed_by_user_email}.")
            return

        book.is_borrowed = True
        book.borrowed_by_user_email = user.email
        
        print(Fore.GREEN + f"Success: {user.name} has borrowed '{book.title}'.")

    def return_book(self, book_id: int, email: str) -> None:
        book = self.book_repository.get_by_id(book_id)

        if not book:
            print(Fore.RED + "Error: Book not found.")
            return

        if not book.is_borrowed:
            print(Fore.YELLOW + "Notice: This book is already in the library.")
            return

        if book.borrowed_by_user_email != email:
            print(Fore.RED + "Access Denied: You cannot return a book borrowed by someone else.")
            return

        book.is_borrowed = False
        book.borrowed_by_user_email = ""
        
        print(Fore.GREEN + f"Success: '{book.title}' has been returned.")

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return self.book_repository.get_by_id(book_id)

    def get_all(self) -> List[Book]:
        return self.book_repository.get_all()
