class Book:
    def __init__(self, title, author="Unknown"):
        self.author = author
        self.title = title
        self._available = True

    def display_info(self):
        print(f"title: {self.title}")
        print(f"author: {self.author}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class Ebook(Book):
    def __init__(self, title, author="Unknown", file_size=None):
        super().__init__(title, author)
        self.file_size = file_size
    
    def display_info(self):
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"file_size: {self.file_size}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Size: {self.file_size}"
        

book1 = Book("Python and its working", "Chatgpt")
# book1.display_info()
book2 = Ebook("Python developer", "chatgpt", 2.3)
# book2.display_info()


class Library:
    def __init__(self):
        self.books: list = []

    def __str__(self):
        return f"book: {self.books}"


    def add_book(self, book): # only to store the Book class object. not to take details.
        self.books.append(book)
        # we need to pass detailed object of the class Book. then it add to the list books

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def show_all_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self,title):
        book = self.find_book(title)
        if book is None:
            print(f"Book {title} is not in library database.")
            return None

        if book._available:
            book._available = False
            print(f"Book {title} has already borrowed.")
        else:
            print(f"{book} is currently checked out.")

    def return_book(self, title):
        book = self.find_book(title)

        # Step 1: Check if book exists in the library
        if book is None:
            print(f"Error: '{title}' does not belong to this library.")
            return

        # Step 2: Check book._available
        if not book._available:
            book._available = True  # Mark available
            print(f"Success: Thank you for returning {title}.")
        else:
            print(f"Notice: {title} was not borrowed. It is already here.")

    def get_available_books(self):
        available_books = []
        for book in self.books:
            if book._available == True:
                available_books.append(book)
        return available_books

    def get_borrowed_books(self):
        borrowed_books = []
        for book in self.books:
            if book._available == False:
                borrowed_books.append(book)
        return borrowed_books



    def borrow_all_available_books(self):
        borrowed_books = len(self.get_available_books())
        for book in self.get_available_books():
            self.borrow_book(book.title)
        return borrowed_books

    # def find_borrowed_books(self, title):
        # for book in self.books




        
library1 = Library()
book3 = Book("Panchtantra")
book4 = Book("Working with data", "chatgpt")
book5 = Ebook("32 people working together", "Chatgpt", 4.5)


library1.add_book(book3)
library1.add_book(book4)
library1.add_book(book5)
# print(library1.books)
# print(library1.find_book("Panchtantra"))
# print(library1.show_all_books)
# library1.show_all_books()
library1.find_book("Working with data")
# library1.borrow_book("Panchtantra")
# library1.borrow_book("Panchtantra")
library1.return_book("Working with data")
# print(library1.get_available_books())
# available_books = library1.get_available_books()
# library1.borrow_all_available_books()
# for book in available_books:
#     print(book.title)

# available_books = library1.get_available_books()
# for book in available_books:
#     print(book.title)

library1.borrow_book("Panchtantra")

library1.borrow_all_available_books()
library1.get_borrowed_books()
# library1.find_borrowed_books("Pnachtantra")


# Output 
# nilesh@nilesh-HP:~/Data/imp_data/GItHub Repo/Python-Question-Solutions$ python3 lib.py
# title: Python and its working
# author: Chatgpt
# title: Python developer
# author: chatgpt
# file_size: 2.3
# Title: Panchtantra, Author: Unknown
# Book Title: Panchtantra, Author: Unknown has already borrowed.
# Title: Panchtantra, Author: Unknown is currently checked out.
# Notice: Title: Working with data, Author: chatgpt was not borrowed. It is already here.

# nilesh@nilesh-HP:~/Data/imp_data/GItHub Repo/Python-Question-Solutions$ python3 lib.py
# Title: Panchtantra, Author: Unknown
# Book Title: Panchtantra, Author: Unknown has already borrowed.
# Title: Panchtantra, Author: Unknown is currently checked out.
# Notice: Title: Working with data, Author: chatgpt was not borrowed. It is already here.

# nilesh@nilesh-HP:~/Data/imp_data/GItHub Repo/Python-Question-Solutions$ python3 lib.py
# Book Title: Panchtantra, Author: Unknown has already borrowed.
# Title: Panchtantra, Author: Unknown is currently checked out.
# Notice: Title: Working with data, Author: chatgpt was not borrowed. It is already here.

# nilesh@nilesh-HP:~/Data/imp_data/GItHub Repo/Python-Question-Solutions$ python3 lib.py
# Book Panchtantra has already borrowed.
# Title: Panchtantra, Author: Unknown is currently checked out.
# Notice: Working with data was not borrowed. It is already here.