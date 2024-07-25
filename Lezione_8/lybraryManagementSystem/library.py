
class Book:

    

    def __init__(self,title: str, author: str, isbn: int, prestato: bool) -> None:

        self.title: str = title
        self.author: str = author
        self.isbn: int = isbn
        self.prestato: bool = prestato

    @classmethod
    def from_string(self,stringa: str) -> object:

        stringa_splittata: list[str] = stringa.split(",")

        title: str = stringa_splittata[0].strip()
        author: str = stringa_splittata[1].strip()
        isbn: int = int(stringa_splittata[2].strip())
        prestato: bool = False

        return Book(title,author,isbn,prestato)
    
    def __str__(self) -> str:
        
        stringa: str = f"Book\nTitolo: {self.title}\nAutore: {self.author}\nISBN: {self.isbn}\nPrestato: {self.prestato}\n"

        return stringa
    
    def __eq__(self, value: object) -> bool:
        
        if isinstance(value,Book):

            return value.isbn == self.isbn
        
        return False



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

        self.borrowed_books.remove(book)
                     #remove non funzionava perchè book.prestato = False veniva eseguito prima di remoev e quindi l'loggetto passato era cambiato
        for i in range(len(libreria.books)):

            if book == libreria.books[i]:
                libreria.books[i].prestato = False

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






class Library:
    
    def __init__(self,books: list[Book] = [], members: list[Member] = []) -> None:
        
        self.books: list[Book] = books
        self.members: list[object] = members

    def add_book(self,book: Book) -> None:

        lista_isbn: list[int] = []

        for i in self.books:

            lista_isbn.append(i.isbn)


        if book.isbn not in lista_isbn:
            self.books.append(book)
            print("Libro aggiunto correttamente!")
            for i in self.books:

                print(i)

        else:

            print("Impossibile aggiungere il libro alla libreria perchè è gia presente.")

    def remove_book(self,book: Book) -> None:

        self.books.remove(book)
        print("Libro rimosso corettamente")
        self.get_books()

    def register_member(self,member: Member) -> None:

        self.members.append(member)
        print("Utente registrato correttamente")

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



#Un libro con lo stesso nome può essere aggiunto alla libreria ma deve avere un ISBN diverso.   riga 67 funzione add_book() classe: Library

    def get_books(self):

        for i in self.books:

            print(i)






nuova_libreria: Library = Library()

print(f"{nuova_libreria.books,nuova_libreria.members}\n")

gey: Member = Member.from_string("Geymark,ciao123")

print(f"{gey}\n")

commedia: Book = Book.from_string("La Divina Commedia, Dante Alighieri, 999000666")
print(f"{commedia}\n")

nuova_libreria.add_book(commedia)

nuova_libreria.lend_book(commedia,gey)
nuova_libreria.register_member(gey)
nuova_libreria.lend_book(commedia,gey)

print("Dopo operazioni\n\n\n")
nuova_libreria.get_books()
print(f"{gey}\n")

gey.return_book(commedia,nuova_libreria)

#nuova_libreria.get_books()  I TEST SI FANNO CON I PRINT, QUINDI DEVONO ESSERE IMPOSTATI BENE, ALTRIMENTI SI POTREBBERO DARE PER SBAGLIATO DELLE COSE GIUSTE

print("dopo rimozione")
nuova_libreria.remove_book(commedia)


#definire il metodo __eq__ in tutti e 3 le classi