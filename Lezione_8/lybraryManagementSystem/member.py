from book import Book



class Member:
    
    
    
    def __init__(self,name: str, member_id: str, borrowed_books: list[Book]) -> None:
        

        self.name: str = name
        self.member_id: str = member_id
        self.borrowed_books: list[Book] = borrowed_books


    @classmethod
    def from_string(self,stringa: str) -> object: #name,member_id

        stringa_splittata: list[str] = stringa.split(",")

        name: str = stringa_splittata[0].strip()
        member_id: str = stringa_splittata[1].strip()
        borrowed_books: list[Book] = []

        return Member(name,member_id,borrowed_books)

    def borrow_book(self,book: Book) -> None:

        self.borrowed_books.append(book)

    
    def return_book(self,book: Book, libreria: object) -> None:

        book.prestato = False
        self.borrowed_books.remove(book)
        libreria.books.append(book)
        print("Libro restituito con successo")
        print(f"Lista libri noleggiati:")
        self.stampa_libri()
        

    def stampa_libri(self) -> str:
            
        stringa : str = ""

        for i in self.borrowed_books:

            stringa += i.__str__()

        return stringa

    def __str__(self) -> str:
        
        stringa: str = f"Member\nNome: {self.name}\nMember id: {self.member_id}\nLibri noleggiati: {self.stampa_libri()}"

        return stringa
    
    def __eq__(self, value: object) -> bool:
        
        if isinstance(value,Member):

            return value.member_id == self.member_id
        return False
    