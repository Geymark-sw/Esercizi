class Documento:

    def __init__(self, testo: str) -> None:

        self.testo: str = testo

    def getText(self)->str:

        return self.testo
    
    def setText(self, testo: str) -> None:

        self.testo = testo

    
    def isInText(self, parola: str) -> bool:

        if parola in self.testo:

            return True
        else:
            return False
        

class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo_messaggio: str) -> None:
        super().__init__(testo)
        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo_messaggio: str = titolo_messaggio

    def getMittente(self) -> str:

        return self.mittente
    
    def getDestinatario(self) -> str:

        return self.mittente
    
    def getTitolo_messaggio(self) -> str:

        return self.titolo_messaggio
    
    def setMittente(self, mittente: str) -> None:

        self.mittente = mittente

    def setDestinatario(self, destinatario: str) -> None:

        self.destinatario = destinatario

    def setTitolo_messaggio(self, titolo_messaggio: str) -> None:

        self.titolo_messaggio = titolo_messaggio

    def getText(self) -> str:
        
        risultato: str = f"Da: {self.mittente}, A: {self.destinatario}\n\
    Titolo: {self.titolo_messaggio}\n\
                        Messaggio: {super().getText()}"
        
        return risultato

    def writeToFile(self) -> None:

        with open("file.txt","w") as reader:
            
            reader.write(self.getText())
        

e: Email = Email("Bella a tutti ragazzi","Gey","Dexter","Questo è titolo del messaggio")

e.writeToFile()

    
    
    
    