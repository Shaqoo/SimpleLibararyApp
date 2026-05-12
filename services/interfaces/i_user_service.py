from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.user import User


class IUserService(ABC):

    @abstractmethod
    def register_user(self, name: str, email: str, password: str) -> None:
        pass

    @abstractmethod
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

    @abstractmethod
    def get_current_user(self) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def seed_admin(self) -> None:
        pass