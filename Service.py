import Library

lib = Library.Library

def search(name:str):
    numb: int = 0
    for book in lib.book_list:
        if(book.name.lower().__contains__(name)):
            print("\n\n--Book found!---")
            book.display_book_info()
        
        if name.lower() == "all":
            numb += 1
            print("\t - ", numb, book.name)
            if numb >= len(lib.book_list):
                menu()
                return
    
        if name == "":
            print("\n\n--Please, entry a book!---")
            menu()
            return
        
        if name == "exit":
            exit()
            
    return
            
def menu():
    foundBook = input("\nSearch for a book:\n\nMENU:\n\tType: 'all' to see all books\n\tType: name of the book (e.g 'python') to search and display\n\tType: 'exit' to exit\n\n>>\t")
    search(foundBook.lower().strip())

def exit():
    print("Bye")
    exec(quit())
menu()