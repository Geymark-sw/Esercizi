from Pagamento import Pagamento

class PagamentoContanti(Pagamento):

    def __init__(self, _importoPagamento: float = None):
        super().__init__(_importoPagamento)

    def dettagliPagamento(self) -> str:
        
        return f"Pagamento in contanti di {self.get_importoPagamento()} €"
    
    def inPezziDa(self) -> str:

        soldi : list = [500,200,100,50,20,10,5,2,1,0.50,0.2,0.1,0.5,0.01]

        valore: float = self.get_importoPagamento()

        cont: int = 0

        print(f"{valore} € da pagare in contanti con:")

        for i in soldi:
            
            if valore == 0:
                break

            if valore - i >= 0:

                while valore - i >= 0:

                    valore = round(valore - i, 2)#dopo la virgola sono i numeri da non approssimare
                    cont += 1

                if i > 2:
                    print(f"{cont} banconota/e da {i} €")
                    

                else:

                    print(f"{cont} moneta/e da {i} €")
                    

                cont = 0



p: PagamentoContanti = PagamentoContanti()
p.set_importoPagamento(1000.75)

p.inPezziDa()
                






                


    
