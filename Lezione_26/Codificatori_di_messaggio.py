from abc import ABC, abstractmethod
import string

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(testoInChiaro: str) -> str:
        pass


class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(testoDecodificato: str) -> str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self,chiave: int) -> None:

        self.chiave: int = chiave
        self.alfabeto: str = string.ascii_lowercase

    def codifica(self,testoInChiaro: str) -> str:

        testoCifrato: str = None

        for i in range(len(testoInChiaro)):

            testoCifrato.

        return testoInChiaro
    
    def decodifica(testoDecodificato: str) -> str:
        pass
    


ces: CifratoreAScorrimento = CifratoreAScorrimento(3)

testoInChiaro: str = input("Inserisci il testo da cifrare:")

print(ces.codifica(testoInChiaro))



    
