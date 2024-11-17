class LibraryBook:
    def __init__(self, isbn, title, author):
        
        self.__isbn = isbn  
        self._title = title  
        self._author = author  
        self._status = "available"  

    def get_ISBN(self):
        
        return self.__isbn

    def _display_basic_info(self):
        
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")

    def borrow_book(self, borrower_name):
        
        if self._status == "available":
            self._status = "borrowed"
            print(f"The book '{self._title}' has been borrowed by {borrower_name}.")
        else:
            print(f"Sorry, the book '{self._title}' is currently unavailable.")


class DigitalLibraryBook(LibraryBook):
    def __init__(self, isbn, title, author, file_format):
        
        super().__init__(isbn, title, author)
        self.file_format = file_format  

    def display_basic_info(self):
        """Display the book's basic and digital information."""
        print("Digital Book Information:")
        self._display_basic_info()  
        print(f"File Format: {self.file_format}")




book = LibraryBook("23-45-79-11", "Science", "Mezbah ")

print("Masked ISBN:", book.get_ISBN())

book.borrow_book("Charu")

digital_book = DigitalLibraryBook("97-65-21-00", "Physics", "Tonmoy", "PDF")


digital_book.display_basic_info()
