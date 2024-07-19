class Calcolatrice:

    def __init__(self,a: int,b: int) -> None:

        self.a: int = a
        self.b: int = b

    def somma(self) -> int:

        return self.a + self.b
    
    def sottrazione(self) -> int:

        return self.a - self.b
    
    def moltiplicazione(self) -> int:

        return self.a * self.b
    
    def divisione(self) -> float:

        return self.a / self.b


print("ciao")
    
