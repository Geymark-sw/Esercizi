from book import Book



class Member:
    
    
    
    def from_string(self,stringa: str) -> object: #name,member_id

        stringa_splittata: list[str] = stringa.split(",")

        self.name: str = stringa_splittata[0].strip()
        self.member_id: str = stringa_splittata[1].strip()
        self.borrowed_books: list[Book] = []

    def borrow_book(self,book: Book) -> None:

        self.borrowed_books.append(book)

    
    def return_book(self,book: Book, libreria: object) -> None:

        self.borrowed_books.remove(book)
        libreria.books.append(book)
        print("Libro restituito con successo")
        print(f"Lista libri noleggiati:")
        for i in self.borrowed_books:
            print(i)
        

    def stampa_libri(self) -> str:
            
        stringa : str = ""

        for i in self.borrowed_books:

            stringa += i.__str__()

        return stringa

    def __str__(self) -> str:
        
        stringa: str = f"Member\nNome: {self.name}\nMember id: {self.member_id}\nLibri noleggiati: {self.stampa_libri()}"

        return stringa