class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrower = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        #instance of class book
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Book "{title}" by {author} added to the library.')

    def display_available_books(self):
        available_books = []
        for book in self.books:
            if not book.is_borrowed:
                available_books.append(book)
        
        if not available_books:
            print("No available books in the library.")
            return

        print("Available books:")
        for book in available_books:
            print(f'Title: {book.title}, Author: {book.author}')

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("All books:")
        for book in self.books:
            if book.is_borrowed:
                status = "Borrowed"
                borrower_info = f", Borrower: {book.borrower}"
            else:
                status = "Available"
                borrower_info = ""
            print(f'Title: {book.title}, Author: {book.author}, Status: {status}{borrower_info}')

    def borrow_book(self, title, borrower_name):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    print(f'Sorry, the book "{title}" is currently borrowed by {book.borrower}.')
                else:
                    book.is_borrowed = True
                    book.borrower = borrower_name
                    print(f'You have borrowed "{title}".')
                return
        print(f'The book "{title}" is not available in the library.')

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    book.borrower = None
                    print(f'You have returned "{title}".')
                else:
                    print(f'The book "{title}" was not borrowed.')
                return
        print(f'The book "{title}" is not available in the library.')

if __name__ == "__main__":
    lib = Library()
    lib.add_book("Ramayana", "Valmiki")
    lib.add_book("Mahabharata", "Vyasa")
    lib.add_book("Ponniyin Selvan", "Kalki Krishnamurthy")
    lib.add_book("The Notebook", "Nicholas Sparks")
    lib.add_book("Romeo and Juliet", "William Shakespeare")
    lib.add_book("Love Story", "Erich")
    lib.add_book("Think and Grow Rich", "Napoleon Hill")
    lib.add_book("The Power of Positive Thinking", "Norman Vincent ")
    lib.add_book("Awaken the Giant Within", "Tony Robbins")
    lib.add_book("The 7 Habits of Highly Effective People", "Stephen")

    print("Welcome to the Library. Enter an option.")
    while True:
        print("\n1. Display available books")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Quit")
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            lib.display_available_books()
        elif user_choice == 2:
            lib.display_all_books()
        elif user_choice == 3:
            title = input("Enter the title of the book you want to borrow: ")
            borrower_name = input("Enter your name: ")
            lib.borrow_book(title, borrower_name)
        elif user_choice == 4:
            title = input("Enter the title of the book you want to return: ")
            lib.return_book(title)
        elif user_choice == 5:
            print("Thank you for using the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")