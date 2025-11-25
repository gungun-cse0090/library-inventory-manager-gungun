# -------- BOOK CLASS --------
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"


# -------- LIBRARY INVENTORY --------
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added.\n")

    def issue_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if b.status == "available":
                    b.status = "issued"
                    print("Book issued.\n")
                else:
                    print("Already issued.\n")
                return
        print("Book not found.\n")

    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if b.status == "issued":
                    b.status = "available"
                    print("Book returned.\n")
                else:
                    print("Book was not issued.\n")
                return
        print("Book not found.\n")

    def show_all(self):
        if not self.books:
            print("No books.\n")
        else:
            for b in self.books:
                print(b)


# -------- MENU --------
def menu():
    lib = Library()

    while True:
        print("\n1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            lib.add_book(Book(title, author, isbn))

        elif ch == "2":
            isbn = input("Enter ISBN to issue: ")
            lib.issue_book(isbn)

        elif ch == "3":
            isbn = input("Enter ISBN to return: ")
            lib.return_book(isbn)

        elif ch == "4":
            lib.show_all()

        elif ch == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


# -------- RUN PROGRAM --------
menu()
