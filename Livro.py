class Livro:
    name: str
    autor: str
    year: str
    isbn: str
    isBorrowed: bool

    def __init__(self, name, autor, year, isbn, isBorrowed):
        self.name = name
        self.autor = autor
        self.year = year
        self.isbn = isbn
        self.isBorrowed = isBorrowed
    
    def display_book_info(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.autor}")
        print(f"Year: {self.year}")
        print(f"ISBN: {self.isbn}")
        print(f"Borrowed: {self.isBorrowed}")


