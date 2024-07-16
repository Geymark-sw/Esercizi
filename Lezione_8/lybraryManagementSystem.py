class Book:

    @classmethod
    def from_string(self,stringa: str) -> object:

        stringa_splittata: list[str] = stringa.split(",")

        self.title: str = stringa_splittata[0].strip()
        self.author: str = stringa_splittata[1].strip()
        self.isbn: int = int(stringa_splittata[2].strip())
        self.prestato: bool = False

        return self
    
    def __str__(self) -> str:
        
        stringa: str = f"Book\nTitolo: {self.title}\nAutore: {self.author}\nISBN: {self.isbn}\nPrestato: {self.prestato}\n"

        return stringa
    
class Member:

    @classmethod
    def from_string(self,stringa: str) -> object:

        stringa_splittata: list[str] = stringa.split(",")

        self.name: str = stringa_splittata[0].strip()
        self.member_id: str = stringa_splittata[1].strip()
        self.borrowed_books: list[Book] = []

    def borrow_book(self,book: Book) -> None:

        self.borrowed_books.append(book)


    def return_book(self,book: Book) -> None:

        self.borrowed_books.remove(book)

    def stampa_libri(self) -> str:
            
        stringa : str = None

        for i in self.borrowed_books:

            stringa += i

        return stringa

    def __str__(self) -> str:

        
        
        stringa: str = f"Member\nNome: {self.name}\nMember id: {self.member_id}\nLibri noleggiati: {self.stampa_libri()}"

        return stringa
    

class Library:

    def __init__(self,books: list[Book], members: list[Member]) -> None:

        self.books: list[Book] = books
        self.members: list[Member] = members

    def add_book(self,book: Book) -> None:

        self.books.append(book)

    def remove_book(self,book: Book) -> None:

        self.books.remove(book)

    def register_member(self,member: Member) -> None:

        self.members.append(member)

    def lend_book(self,book: Book, member: Member) -> None:

        if book.prestato == False and member in self.members:

            book.prestato = True
            member.borrow_book(book)

            print(f"Prestito effettuato con successo!\n")
            print(f"Libro:\n{book}")
            print(f"Membro:\n{member}")

        elif book.prestato == True:

            print("Prestito non effettuabile. Il libro è gia stato prestato")

        else:

            print("Prestito non effettuabile. L'utente non è registrato")



#Un libro con lo stesso nome può essere aggiunto alla libreria ma deve averu un ISBN diverso.   riga 67 funzione add_book() classe: Library
    


    















