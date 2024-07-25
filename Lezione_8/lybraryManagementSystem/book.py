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