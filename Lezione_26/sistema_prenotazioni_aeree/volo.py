from abc import ABC,abstractmethod

class Volo(ABC):

    def __init__(self,codice_volo: str, posti_disponibili_a: int) -> None:

        self.codice_volo: str = codice_volo 
        self.posti_disponibili_a: int = posti_disponibili_a
        self.prenotazioni: int = 0

    
    @abstractmethod
    def prenota_posto(self) -> None:

        pass

    @abstractmethod
    def posti_disponibili(self) -> dict[str:int]:

        pass


class VoloCommerciale(Volo):

    def __init__(self, codice_volo: str, posti_disponibili_a: int) -> None:
        super().__init__(codice_volo, posti_disponibili_a)
        self.posti_economica: int = posti_disponibili_a * 70 // 100
        self.posti_business: int = posti_disponibili_a * 20 // 100
        self.posti_prima: int = posti_disponibili_a - self.posti_economica + self.posti_business
        self.posti_disponibili_a = self.posti_economica + self.posti_business + self.posti_prima #ricalcolo posti disponibili
        self.capacità_massima: int = self.posti_disponibili_a

        self.prenotazioni_economica: int = 0
        self.prenotazioni_business: int = 0
        self.prenotazioni_prima: int = 0


    def posti_disponibili(self) -> dict[str:int]:
        
        dizionario: dict[str:int] = {"capacità_massima":self.capacità_massima, "posti_disponibili":self.posti_disponibili_a, 
                                     "classe_economica":self.posti_economica, "classe_business":self.posti_business, "classe prima":self.posti_prima}
        
        if self.posti_disponibili_a == 0:

            print(f"Volo {self.codice_volo} al completo!")

        return dizionario
    
    def prenota_posto(self,posti: int, classe_servizio: int) -> None:

        while classe_servizio != 1 and classe_servizio != 2 and classe_servizio != 3:

            print("La classe servizio inserita è errata")
            
            classe_servizio = int(input("Inserisci il numero della classe servizio:\n"
                  "1 - Economica\n2 - Business\n 3 - Prima classe"))
            
            
        
        while posti > self.posti_disponibili_a:

            if self.posti_disponibili_a == 0:

                print("Ci dispiace, ma il volo è al completo, non puoi prenotare nessun posto.")
                break

            print("Il numero di posti che si sta cercando di prenotare è maggiore ai posti disponibili!")
            print(f"Puoi prenotare fino ad un massimo di {self.posti_disponibili_a} posti")
            posti = int(input("Inserisci un numero di posti: "))

        if classe_servizio == 1:

            while posti > self.posti_economica:

                print("Il numero di posti che si sta cercando di prenotare è maggiore ai posti disponibili nella classe Economica")
                print(f"Puoi prenotare fino ad un massimo di {self.posti_economica} posti nella classe Economica")
                posti = int(input("Inserisci un nunero di posti: "))

            self.posti_economica -= posti
            self.prenotazioni_economica += posti
            self.prenotazioni += posti

            print("Operazione andata a buon fine!")
            print(f"Sono stati prenotati {posti} sul volo {self.codice_volo} nella classe Economica")

        elif classe_servizio == 2:

            while posti > self.posti_business:

                print("Il numero di posti che si sta cercando di prenotare è maggiore ai posti disponibili nella classe Business")
                print(f"Puoi prenotare fino ad un massimo di {self.posti_business} posti nella classe Business")
                posti = int(input("Inserisci un nunero di posti: "))

            self.posti_business -= posti
            self.prenotazioni_business += posti
            self.prenotazioni += posti

            print("Operazione andata a buon fine!")
            print(f"Sono stati prenotati {posti} sul volo {self.codice_volo} nella classe Business")


        else:

            while posti > self.posti_prima:

                print("Il numero di posti che si sta cercando di prenotare è maggiore ai posti disponibili nella Prima classe")
                print(f"Puoi prenotare fino ad un massimo di {self.posti_economica} posti nella Prima classe")
                posti = int(input("Inserisci un nunero di posti: "))

            self.posti_prima -= posti
            self.prenotazioni_prima += posti
            self.prenotazioni += posti

            print("Operazione andata a buon fine!")
            print(f"Sono stati prenotati {posti} sul volo {self.codice_volo} nella classe Economica")


    def __eq__(self, value: object) -> bool:
        
        if isinstance(value, Volo):

            return value.codice_volo == self.codice_volo
        
        return False
    

class VoloCharter(Volo):

    def __init__(self, codice_volo: str, posti_disponibili_a: int, prezzo: float) -> None:
        super().__init__(codice_volo, posti_disponibili_a)
        self.prezzo: float  = prezzo

    def posti_disponibili(self) -> int:
        
        return self.posti_disponibili_a
    
    def prenota_posto(self) -> None:
        
        if self.posti_disponibili_a != 0:

            self.posti_disponibili_a = 0
            self.prenotazioni = 1
            print(f"Volo {self.codice_volo}prenotato con successo!")
            print(f"Prezzo: {self.prezzo} €")

        else:

            print(f"Impossibile prenotare il volo.\nIl volo {self.codice_volo} è già stato prenotato")




class CompagniaAerea:

    def __init__(self, nome_compagnia: str, prezzo_standard: float, flotta: list[VoloCommerciale] = []) -> None:

        self.nome_compagnia: str = nome_compagnia
        self.prezzo_standard: float = prezzo_standard
        self.flotta: list[VoloCommerciale] = flotta

    def aggiungi_volo(self, volo_commerciale: VoloCommerciale) -> None:

        if volo_commerciale not in self.flotta:

            self.flotta.append(volo_commerciale)
            print(f"Volo {volo_commerciale.codice_volo} aggiunto correttamente alla flotta")
        else:
            print(f"Il volo {volo_commerciale.codice_volo} è già pressente nella flotta, di conseguenza non può essere aggiunto")

    def rimuovi_volo(self, volo_commerciale: VoloCommerciale) -> None:

        if volo_commerciale in self.flotta:

            self.flotta.remove(volo_commerciale)
            print(f"Volo {volo_commerciale.codice_volo} rimosso correttamente dalla flotta")

        else:
            print(f"Il volo {volo_commerciale.codice_volo} non è presente nella flotta, di conseguenza non può essere rimosso")


    def mostra_flotta(self) -> None:
        
        print(f"Elenco flotta della compagnia aerea {self.nome_compagnia}:")
        for i in self.flotta:
            print(f"Volo commerciale {i.codice_volo}")

    def guadagno(self) -> float:

        guadagno: float = 0

        for i in self.flotta:

            guadagno += i.posti_economica * self.prezzo_standard
            guadagno += i.posti_business * self.prezzo_standard * 2
            guadagno += i.posti_prima * self.prezzo_standard * 3

        return round(guadagno,2)
    
    



            

        

        

        




        

            
        




