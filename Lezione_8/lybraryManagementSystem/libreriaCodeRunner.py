class Member:
    def __init__(self, member_id: str, name: str) -> None:
        
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = []
        
    def borrow_book(self, book):
        
        if book not in self.borrowed_books and book.is_borrowed == False:
            
            self.borrowed_books.append(book)
            
    def return_book(self, book) -> None:
        
        if book in self.borrowed_books:
            
            self.borrowed_books.remove(book)
            
    def __eq__(self, other: object) -> None:
        
        if isinstance(other, Member):
            
            return other.member_id == self.member_id
        return False
            

class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool = False) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed = is_borrowed
        
    def borrow(self) -> None:
        
        if self.is_borrowed == False:
            self.is_borrowed = True
    def return_book(self) -> None:
        
        if self.is_borrowed == True:
            
            self.is_borrowed = False
            
    def __eq__(self, other: object) -> None:
        
        if isinstance(other, Book):
            return self.book_id == other.book_id
        return False

class Library:
    
    def __init__(self) -> None:
        
        self.books: dict[str:Book] = {}
        self.members: dict[str:Member] = {}
        
    def add_book(self,book_id: str, title: str, author: str) -> None:
        
        b: Book = Book(book_id,title,author)
        
        if b not in self.books.values():
            
            self.books[b.book_id] = b
            
    def register_member(self,member_id: str, name:str) -> None:
        
        m: Member = Member(member_id,name)
        
        if m not in self.members.values():
            
            self.members[m.member_id] = m
            
    def borrow_book(self, member_id: str, book_id: str) -> None:
        
        if book_id not in self.books.keys():

            raise ValueError("Book not found")
        
        if not self.books[book_id].is_borrowed and member_id in self.members.keys() and book_id in self.books.keys():
            
            self.books[book_id].is_borrowed = True
            self.members[member_id].borrowed_books.append(self.books[book_id])

        elif member_id not in self.members.keys():

            raise ValueError("Member not found")
        

        else:

            raise ValueError("Book is already borrowed")
            
    def return_book(self, member_id: str, book_id: str) -> None:

        lista_nomi: list[str] = []

        for i in self.members[member_id].borrowed_books:

            lista_nomi.append(i.book_id)
        
        if self.books[book_id].is_borrowed and member_id in self.members.keys() and book_id in lista_nomi:
            
            self.members[member_id].borrowed_books.remove(self.books[book_id])
            self.books[book_id].is_borrowed = False
        else:
            
            raise ValueError("Book not borrowed by this member")
            


    def get_borrowed_books(self, member_id: str) -> list:
        
        lista_nomi: list = []
        
        if self.members[member_id].borrowed_books:
            
            for i in self.members[member_id].borrowed_books:
                lista_nomi.append(i.title)
        
        return lista_nomi
    
library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")


 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")


# Edge case - trying to borrow a book by a non-existent member
try:
    library.borrow_book("M004", "B001")
except ValueError as e:
    print(e)