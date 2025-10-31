books = {
    "101": {
        "book_name": "The Jungle Book",
        "author_name": "Rudyard Kipling",
        "year_published": "1894",
        "number_of_copies": 5,
        "status": True
    },
    "102": {
        "book_name": "To Kill a Mockingbird",
        "author_name": "Harper Lee",
        "year_published": "1960",
        "number_of_copies": 5,
        "status": True
    },
    "103": {
        "book_name": "1984",
        "author_name": "George Orwell",
        "year_published": "1949",
        "number_of_copies": 5,
        "status": True
    },
    "104": {
        "book_name": "Pride and Prejudice",
        "author_name": "Jane Austen",
        "year_published": "1813",
        "number_of_copies": 5,
        "status": True
    },
    "105": {
        "book_name": "The Great Gatsby",
        "author_name": "F. Scott Fitzgerald",
        "year_published": "1925",
        "number_of_copies": 5,
        "status": True
    }
}


def add_books(x):
    book_id = input("Enter book id: ")
    if book_id in x:
        print("Error: Book already exists")
        return False

    x[book_id] = {
        "book_name": "",
        "author_name": "",
        "year_published": "",
        "number_of_copies": 0,
        "status": True
    }

    x[book_id]["book_name"] = input("Enter book name: ")
    x[book_id]["author_name"] = input("Enter author name: ")
    x[book_id]["year_published"] = input("Enter year published: ")
    x[book_id]["number_of_copies"] = int(input("Enter number of copies: "))
    status_input = input("Enter status (True/False): ").strip().lower()
    x[book_id]["status"] = status_input in ("true", "yes", "available", "1")

    print(" Book added successfully")
    return True

#  Find Book
def find_book(books_dict):
    book_id = input("Enter book ID to find: ").strip()
    if book_id in books_dict:
        print("Book found")
        print(books_dict[book_id])
        return books_dict[book_id]
    else:
        print("Book not found")
        return {}

#  Borrow Book
def borrow_book(books_dict):
    book_id = input("Enter book ID to borrow: ").strip()
    if book_id in books_dict:
        book = books_dict[book_id]
        if book["number_of_copies"] > 0:
            book["number_of_copies"] -= 1
            print(f"You borrowed '{book['book_name']}'. Copies left: {book['number_of_copies']}")
            if book["number_of_copies"] == 0:
                book["status"] = False
        else:
            print("No copies left for this book.")
    else:
        print("Book ID not found.")

# Return Book
def return_book(books_dict):
    book_id = input("Enter book ID to return: ").strip()
    if book_id in books_dict:
        book = books_dict[book_id]
        book["number_of_copies"] += 1
        book["status"] = True
        print(f"Book returned successfully! Copies now: {book['number_of_copies']}")
    else:
        print("Book ID not found.")

#  Display All Books
def display_all_books(books_dict):
    if not books_dict:
        print("No books in library.")
    else:
        print("\n All Books in Library:")
        for book_id, info in books_dict.items():
            print(f"\nBook ID: {book_id}")
            print(f"Book Name: {info['book_name']}")
            print(f"Author Name: {info['author_name']}")
            print(f"Year Published: {info['year_published']}")
            print(f"Copies: {info['number_of_copies']}")
            print(f"Status: {'Available' if info['status'] else 'Borrowed'}")

# Get Available Books
def get_available_books(books_dict):
    available_books = []
    for book_id, info in books_dict.items():
        if info["status"] == True:
            available_books.append((book_id, info))
    return available_books

# Main Menu
def main():
    while True:
        print("\n Welcome to  LIBRARY MENU ...")
        print("1. Add Book")
        print("2. Find Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Available Books")
        print("6. Show All Books")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_books(books)
        elif choice == "2":
            find_book(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            available = get_available_books(books)
            if not available:
                print("No books available.")
            else:
                print("\n Available Books:")
                for book_id, info in available:
                    print(f"{book_id} - {info['book_name']} by {info['author_name']} ({info['number_of_copies']} copies)")
        elif choice == "6":
            display_all_books(books)
        elif choice == "7":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number (1-7).")


main()