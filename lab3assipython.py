# Name: HIMANSHU SAINI

#roll number:2501010201

# Title: LibraryInventor
from inventory import LibraryInventory
from book import Book

inv = LibraryInventory()

def menu():
    while True:
        print("\n--- Library Menu ---")
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
            inv.add_book(Book(title, author, isbn))
            print("Book added.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inv.search_by_isbn(isbn)
            if book and book.issue():
                inv.save_books()
                print("Book issued.")
            else:
                print("Book not available.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inv.search_by_isbn(isbn)
            if book and book.return_book():
                inv.save_books()
                print("Book returned.")
            else:
                print("Book was not issued.")

        elif choice == "4":
            inv.display_all()

        elif choice == "5":
            title = input("Enter title to search: ")
            result = inv.search_by_title(title)
            for b in result:
                print(b)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Try again.")

menu()