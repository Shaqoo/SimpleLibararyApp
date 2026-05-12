from __future__ import annotations
import re

class Validator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        # Basic email pattern: text@text.domain
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def is_strong_password(password: str) -> bool:
        # Minimum 6 characters
        return len(password) >= 6

    @staticmethod
    def is_not_empty(text: str) -> bool:
        return bool(text and text.strip())
