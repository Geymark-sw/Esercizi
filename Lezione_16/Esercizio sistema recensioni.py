class Media:

    def __init__(self) -> None:
        
        self.title: str = None
        self.reviews: list[int] = []



    def set_title(self, title: str):

        self.title: str = title
        print("Il titolo è stato impostato correttamente")

    def get_title(self) -> str:

        return self.title
    
    def aggiungi_valutazione(self,voto: int):

        self.reviews.append(voto)

    def get_media(self) -> float:
        
        media: int = 0

        for i in self.reviews:

            media += i

        return media/len(self.reviews)
    


    def get_rate(self) -> str:

        voti: dict[int:str] = {"1":"Terribile","2":"Brutto","3":"Normale","4":"Bello","5":"Grandioso"}

        for i in voti:

            if str(round(self.get_media())) == i:

                return voti[i]
            
    def rate_percentage(self,voto:int) -> float:

        cont: int = 0

        for i in self.reviews:

            if i == voto:

                cont += 1

        return cont*100/len(self.reviews)
    
    def recensione(self) -> str:

        print(f"Titolo del film: {self.get_title()}\n"
                f"Voto Medio: {self.get_media()}\n"
                f"Giudizio: {self.get_rate()}\n"
                f"Terribile: {self.rate_percentage(1)}%\n"
                f"Brutto: {self.rate_percentage(2)}%\n"
                f"Normale: {self.rate_percentage(3)}%\n"
                f"Bello: {self.rate_percentage(4)}%\n"
                f"Grandioso: {self.rate_percentage(5)}%")
        
class Film(Media):

    def __init__(self) -> None:
        super().__init__()


f1: Film = Film()
f1.set_title("Star Wars")
f1.aggiungi_valutazione(4)
f1.aggiungi_valutazione(5)
f1.aggiungi_valutazione(1)
f1.aggiungi_valutazione(4)

f1.recensione()


        




    





















    