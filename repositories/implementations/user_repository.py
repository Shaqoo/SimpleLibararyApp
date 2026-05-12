from __future__ import annotations
from typing import List, Optional
from entities.user import User
from repositories.interfaces.i_user_repository import IUserRepository
from context.library_context import LibraryContext

class UserRepository(IUserRepository):
    def __init__(self, context: LibraryContext):
        self.context = context
    
    def create_user(self, user: User):
        self.context.users.append(user)

    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self.context.users:
            if user.id == user_id:
                return user
        return None
    
    def get_by_email(self, email: str) -> Optional[User]:
        for user in self.context.users:
            if user.email == email:
                return user
        return None
    
    def get_all(self) -> List[User]:
        return self.context.users