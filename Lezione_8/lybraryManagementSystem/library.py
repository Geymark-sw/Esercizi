
from book import Book
from member import Member






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

nuova_libreria.get_books()

nuova_libreria.remove_book(commedia)


#definire il metodo __eq__ in tutti e 3 le classi