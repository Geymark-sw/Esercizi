def make_album(artista: str, titolo_album: str, numero_brani: int = None) -> dict[str:str, str:str , str:int]:

    if numero_brani:

        dizionario: dict[str:str, str:str, str:int] = {"Artista":artista,"Titolo album":titolo_album,"Numero brani":numero_brani}
        return dizionario
    
    else:

        dizionario: dict[str:str, str:str] = {"Artista":artista,"Titolo album":titolo_album}
        return dizionario


print(make_album("Pippo","Lesgoski"))
print(make_album("Pluto","Leggo",11))
print(make_album("Paperino","Paperopoli"))