from colorama import Fore, init

init(autoreset=True)

class Menu:
    def __init__(self, user_service, book_service):
        self.user_service = user_service
        self.book_service = book_service

    def show(self):
        while True:
            user = self.user_service.get_current_user()
            if not user:
                self.main_menu()
            elif user.role == "admin":
                self.admin_menu()
            else:
                self.customer_menu()

    # =========================
    # 🏠 MENUS
    # =========================
    def main_menu(self):
        print(Fore.CYAN + "\n==== MAIN MENU ====")
        print("1. Register")
        print("2. Login")
        print("0. Exit")
        choice = input("Choose: ").strip()
        
        if choice == "1": self.register()
        elif choice == "2": self.login()
        elif choice == "0": 
            print(Fore.MAGENTA + "Goodbye 👋")
            exit()
        else: print(Fore.RED + "Invalid choice")

    def customer_menu(self):
        user = self.user_service.get_current_user()
        print(Fore.GREEN + f"\n==== CUSTOMER MENU ({user.name}) ====")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Logout")
        choice = input("Choose: ").strip()
        
        if choice == "1": self.view_books()
        elif choice == "2": self.borrow_book()
        elif choice == "3": self.return_book()
        elif choice == "4": self.user_service.logout()

    def admin_menu(self):
        print(Fore.YELLOW + "\n==== ADMIN MENU (ADMIN) ====")
        print("1. Add Book")
        print("2. View Books")
        print("3. View Users")
        print("4. Logout")
        choice = input("Choose: ").strip()
        
        if choice == "1": self.add_book()
        elif choice == "2": self.view_books()
        elif choice == "3": self.view_users()
        elif choice == "4": self.user_service.logout()

    # =========================
    # 👤 AUTH ACTIONS
    # =========================
    def register(self):
        print(Fore.WHITE + "\n--- User Registration ---")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        # Validation happens inside UserService
        self.user_service.register_user(name, email, password)

    def login(self):
        print(Fore.WHITE + "\n--- User Login ---")
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        self.user_service.authenticate_user(email, password)

    # =========================
    # 📚 BOOK ACTIONS
    # =========================
    def add_book(self):
        print(Fore.WHITE + "\n--- Add New Book ---")
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        date = input("Date Published (YYYY): ").strip()
        self.book_service.add_book(title, author, date)

    def borrow_book(self):
        try:
            book_id = int(input("Enter Book ID to borrow: "))
            user = self.user_service.get_current_user()
            self.book_service.borrow_book(book_id, user.id)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric Book ID.")

    def return_book(self):
        try:
            book_id = int(input("Enter Book ID to return: "))
            user = self.user_service.get_current_user()
            self.book_service.return_book(book_id, user.email)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric Book ID.")

    def view_books(self):
        books = self.book_service.get_all()
        print(Fore.CYAN + "\n--- Library Catalog ---")
        if not books:
            print("The library is currently empty.")
        for book in books:
            print(book)

    def view_users(self):
        users = self.user_service.get_all_users()
        print(Fore.CYAN + "\n--- Registered Users ---")
        for user in users:
            print(f"- {user.name} ({user.email}) - Role: {user.role}")
