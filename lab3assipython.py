# Name: HIMANSHU SAINI

#roll number:2501010201

# Title: LibraryInventor
import json
import logging
from pathlib import Path

# ---------------------- LOGGING SETUP ------------------------
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------- BOOK CLASS ---------------------------
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        self.status = "available"

    def is_available(self):
        return self.status == "available"


# ----------------- LIBRARY INVENTORY CLASS -------------------
class LibraryInventory:
    def __init__(self, filepath="catalog.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load_catalog()

    def load_catalog(self):
        try:
            if self.filepath.exists():
                with open(self.filepath, "r") as file:
                    data = json.load(file)
                    self.books = [Book(**book) for book in data]
                    logging.info("Catalog loaded successfully.")
            else:
                self.save_catalog()
        except Exception as e:
            logging.error(f"Error loading catalog: {e}")
            self.books = []

    def save_catalog(self):
        try:
            with open(self.filepath, "w") as file:
                json.dump([book.to_dict() for book in self.books], file, indent=4)
            logging.info("Catalog saved successfully.")
        except Exception as e:
            logging.error(f"Error saving catalog: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_catalog()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return self.books


# ---------------------- MAIN MENU ----------------------------
def main():
    inventory = LibraryInventory()

    while True:
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")

            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("\n✔ Book added successfully.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)

            if book and book.issue():
                inventory.save_catalog()
                print("\n✔ Book issued successfully.")
            else:
                print("\n✖ Book not available or already issued.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)

            if book:
                book.return_book()
                inventory.save_catalog()
                print("\n✔ Book returned successfully.")
            else:
                print("\n✖ Book not found.")

        elif choice == "4":
            print("\n--- All Books ---")
            for book in inventory.display_all():
                print(book)

        elif choice == "5":
            search = input("Enter title or ISBN: ")

            if search.isdigit():
                book = inventory.search_by_isbn(search)
                print(book if book else "\n✖ No book found.")
            else:
                results = inventory.search_by_title(search)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("\n✖ No book found.")

        elif choice == "6":
            print("\nThank you! Exiting program...")
            break

        else:
            print("\n✖ Invalid choice. Try again.")


# -------------------- RUN THE PROGRAM ------------------------
if __name__ == "__main__":
    main()
