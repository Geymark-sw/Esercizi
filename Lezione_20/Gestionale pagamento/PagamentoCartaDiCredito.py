from Pagamento import Pagamento

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nomeTitolare: str, dataScadenza: str, numeroCarta: int, _importoPagamento: float = None):
        super().__init__(_importoPagamento)

        self.nomeTitolare: str = nomeTitolare
        self.dataScadenza: str = dataScadenza
        self.numeroCarta: int = numeroCarta

    
    
    def dettagliPagamento(self) -> None:

        print(f"Pagamento di: {self.get_importoPagamento()}€ effettuato con la carta di credito. \n"
              f"Nome sulla carta: {self.nomeTitolare}\n"
              f"Data di scadenza: {self.dataScadenza}\n"
              f"Numero della Carta: {self.numeroCarta}")
        

        
pcdc: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Geymark Emmanuel Papio", "12/25", 1234567890098765, 725.10)
pcdc.dettagliPagamento()

