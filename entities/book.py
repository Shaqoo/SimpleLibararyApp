from __future__ import annotations

class Book:
    def __init__(self, id: int ,title: str, author: str, date_created: str):
        self.id = id
        self.title = title
        self.author = author
        self.date_created = date_created
        self.is_borrowed = False
        self.borrowed_by_user_email = ""
    
    def __str__(self):
        status = "borrowed" if self.is_borrowed else "Available"
        return f"[{self.id}] {self.title} by {self.author} - {status} \nDate Published {self.date_created}"
