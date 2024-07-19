import unittest

from calcolatrice import Calcolatrice



class TestCalcolatrice(unittest.TestCase):
    
    calcolatrice: Calcolatrice = Calcolatrice(6,2)

    def test_somma(self) -> None:

        
        self.assertEqual(self.calcolatrice.somma(),8,"La somma non è giusta")

    def test_sottrazione(self) -> None:

        self.assertEqual(self.calcolatrice.sottrazione(),3,"La sottrazione non è giusta")

    def test_moltiplicazione(self) -> None:

        self.assertEqual(self.calcolatrice.moltiplicazione(),12,"La moltiplicazione non è giusta")

    def test_divisione(self) -> None:

        self.assertEqual(self.calcolatrice.divisione(),3,"La divisione non è giusta")





    