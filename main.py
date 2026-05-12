# main.py

# 1. Import the Context
from context.library_context import LibraryContext

# 2. Import Concrete Repository Implementations
from repositories.implementations.book_repository import BookRepository
from repositories.implementations.user_repository import UserRepository

# 3. Import Concrete Service Implementations
from services.implementations.book_service import BookService
from services.implementations.user_service import UserService

# 4. Import UI
from ui.menu import Menu

def main():
    # --- DATA LAYER ---
    # Create the shared in-memory storage (the list-based context)
    context = LibraryContext()

    # Instantiate Repositories with the context
    # These implement IBookRepository and IUserRepository
    book_repo = BookRepository(context)
    user_repo = UserRepository(context)

    # --- BUSINESS LAYER ---
    # Instantiate Services
    # user_service implements IUserService
    user_service = UserService(user_repo)

    # Seed default admin user
    user_service.seed_admin()
    
    # book_service implements IBookService 
    # (Note: Passed both repos as per your service's __init__)
    book_service = BookService(book_repo, user_repo)

    # --- PRESENTATION LAYER ---
    # Inject services into the Menu
    menu = Menu(user_service, book_service)

    # Start the application
    try:
        menu.show()
    except KeyboardInterrupt:
        print("\n\nApplication closed. Goodbye!")

if __name__ == "__main__":
    main()
