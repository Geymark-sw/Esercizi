class Sala:

    def __init__(self, numero_identificativo: int, film: str, posti_totali: int, posti_disponibili: int):
        
        self.numero_identificativo: int = numero_identificativo
        self.film: str = film
        self.posti_totali: int = posti_totali
        self.posti_disponibili: int = posti_disponibili

s: Sala = Sala()
print(s)