# Simple Library App

A robust, console-based Library Management System built with Python, emphasizing clean architecture, dependency injection, and role-based access control.

## 🚀 Features

### User Management
- **Registration & Login:** Secure user registration with password hashing (SHA-256).
- **Role-Based Access:** Distinct menus and functionalities for **Admins** and **Customers**.
- **Validation:** Built-in validators for emails, strong passwords, and required fields.

### Library Actions
- **Book Management (Admin):** Add new books to the catalog and view all registered users.
- **Borrowing System (Customer):** Browse the catalog, borrow available books, and return them.
- **Concurrency Logic:** Prevents borrowing already-borrowed books and restricts returns to the original borrower.

## 🏗️ Architecture

The project follows an **N-Tier Architecture** to ensure maintainability and scalability:

1.  **Presentation Layer (`ui/`):** Handled by `Menu.py`, providing a colored CLI experience using `colorama`.
2.  **Service Layer (`services/`):** Contains business logic (e.g., `UserService`, `BookService`).
3.  **Repository Layer (`repositories/`):** Manages data access through interfaces, allowing for easy transitions between in-memory storage and future databases.
4.  **Data Layer (`context/` & `entities/`):** Defines the data structures and the shared in-memory context.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd SimpleLibararyApp
   ```

2. **Install dependencies:**
   This project uses `colorama` for terminal styling.
   ```bash
   pip install colorama
   ```

## 🚦 Getting Started

Run the application from the root directory:
```bash
python main.py
```

### Default Admin Credentials
The system automatically seeds an admin account on startup:
- **Email:** `Admin@yopmail.com`
- **Password:** `admin123#`

## 📂 Project Structure
- `main.py`: Application entry point and dependency injection setup.
- `services/`: Implementation of business rules.
- `repositories/`: Data persistence logic.
- `ui/`: Terminal-based user interface.