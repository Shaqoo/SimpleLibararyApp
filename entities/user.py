from __future__ import annotations
class User:
    def __init__(self, id: int, name: str, email: str, password: str, date_created: str, role: str = "customer"):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.date_created = date_created
        self.role = role
    
    def __str__(self):
        return f"Id: [{self.id}] \nName: {self.name} \nEmail: {self.email} \nRole: {self.role} \nDate Registered: {self.date_created}"