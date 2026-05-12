from __future__ import annotations
import hashlib
from datetime import datetime
from typing import Optional, List
from services.interfaces.i_user_service import IUserService
from repositories.interfaces.i_user_repository import IUserRepository
from entities.user import User
from utils.validators import Validator  
from colorama import Fore

class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
        self._current_user: Optional[User] = None

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def _verify_password(self, plain: str, hashed: str) -> bool:
        return self._hash_password(plain) == hashed

    def register_user(self, name: str, email: str, password: str) -> None:
        if not Validator.is_not_empty(name):
            print(Fore.RED + "Registration Error: Name is required.")
            return

        if not Validator.is_valid_email(email):
            print(Fore.RED + f"Registration Error: '{email}' is not a valid email format.")
            return

        if not Validator.is_strong_password(password):
            print(Fore.RED + "Registration Error: Password must be at least 6 characters long.")
            return

        existing_user = self.user_repository.get_by_email(email)
        if existing_user:
            print(Fore.YELLOW + "Registration Error: A user with this email already exists.")
            return

        users = self.user_repository.get_all()
        user_id = max([u.id for u in users], default=0) + 1
        
        date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hashed_password = self._hash_password(password)
        
        user = User(user_id, name, email, hashed_password, date_created)
        self.user_repository.create_user(user)
        print(Fore.GREEN + f"User '{name}' registered successfully! You can now login.")

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        if not email or not password:
            print(Fore.RED + "Error: Please provide both email and password.")
            return None

        user = self.user_repository.get_by_email(email)
        
        if not user:
            print(Fore.RED + "Login Failed: User not found.")
            return None

        if not self._verify_password(password, user.password):
            print(Fore.RED + "Login Failed: Invalid password.")
            return None

        self._current_user = user
        print(Fore.GREEN + f"Welcome back, {user.name}!")
        return user

    def logout(self) -> None:
        if self._current_user:
            print(Fore.MAGENTA + f"Goodbye, {self._current_user.name}. Logged out successfully.")
            self._current_user = None
        else:
            print(Fore.YELLOW + "No user is currently logged in.")

    def get_current_user(self) -> Optional[User]:
        return self._current_user

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.user_repository.get_by_email(email)

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all()
    
    def seed_admin(self) -> None:
        users = self.user_repository.get_all()
        user_id = max([u.id for u in users] , default=0) + 1
        hashed_password = self._hash_password('admin123#')
        date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        user = User(user_id,"Shakirullah","Admin@yopmail.com",hashed_password,date_created,"admin")
        self.user_repository.create_user(user)
        print(Fore.GREEN + f"Admin seeded successfully")
