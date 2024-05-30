class Film:

    def __init__(self, titolo: str, durata: float):

        self.titolo: str = titolo
        self.durata: float = durata

class Sala:

    def __init__(self, numero_identificativo: int, film: Film, posti_totali: int, posti_disponibili: int):
        
        self.numero_identificativo: int = numero_identificativo
        self.film: Film = film
        self.posti_totali: int = posti_totali
        self.posti_disponibili: int = posti_disponibili

    def prenota_posti(self,num_posti) -> None:

        if num_posti <= self.posti_disponibili:
            self.posti_disponibili -= num_posti
            print("Posti confermati correttamente")

        else:
            print("Impossibile eseguire la prenotazione, il numero di"
                  "posti che stai cercando di prenotare è maggiore ai posti disponibile")
            
    def get_posti_disponibili(self) -> int:

        return self.posti_disponibili
    
class Cinema:

    def __init__(self, nome: str, indirizzo: str, sale: list[Sala] = []):

        self.nome: str = nome
        self.indirizzo: str = indirizzo
        self.sale: list[Sala] = sale

    def aggiungi_sala(self, sala: Sala):

        if sala not in self.sale:
            self.sale.append(sala)