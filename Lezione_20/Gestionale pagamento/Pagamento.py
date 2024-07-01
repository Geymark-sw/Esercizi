class Pagamento:

    def __init__(self, _importoPagamento: float = None):

        self._importoPagamento = _importoPagamento

    def get_importoPagamento(self) -> None:

        return self._importoPagamento
    
    def set_importoPagamento(self, importoPagamento) -> None:

        self._importoPagamento = importoPagamento

    def dettagliPagamento(self) -> str:

        return f"L'importo del pagamento è di {self.get_importoPagamento()} €"
    
    def __str__(self) -> str:
        pass
    