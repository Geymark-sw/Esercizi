from Dottore import Dottore
from Paziente import Paziente

class Fattura:

    def __init__(self,lista_pazienti: list[Paziente], dottore: Dottore):

        self.__lista_pazienti: list[Paziente] = lista_pazienti
        self.__dottore: Dottore = dottore

        if dottore.is_a_valid_doctor() == True:
            self.__fatture: int = len(lista_pazienti)
            self.__salary: int = 0

        else:
            self.__lista_pazienti: list[Paziente] = None
            self.__dottore: Dottore = None
            self.__fatture: int = None
            self.__salary: int = None

            print("Impossibile istanziare una fattura poichè il dottore non è valido.")

            