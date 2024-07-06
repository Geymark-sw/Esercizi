def make_album(artista: str, titolo_album: str, numero_brani: int = None) -> dict[str:str, str:str , str:int]:

    if numero_brani:

        dizionario: dict[str:str, str:str, str:int] = {"Artista":artista,"Titolo album":titolo_album,"Numero brani":numero_brani}
        return dizionario
    
    else:

        dizionario: dict[str:str, str:str] = {"Artista":artista,"Titolo album":titolo_album}
        return dizionario


while True:

    artista: str = input("Inserisci il nome dell'artista: ")
    titolo_album: str = input("Inserisci il nome dell'album: ")

    bool_ver: str = input("Vuoi inserire il numero di brani nell'album? Si/No ").lower()

    if bool_ver == "si":
        
        numero_brani: int = input("Inserisci il numero di brani: ")
        print(make_album(artista,titolo_album,numero_brani))

    else:

        print(make_album(artista,titolo_album))

    bool_ver = input("Voui creare un altro Album Dizionario? Si/No ").lower()

    if bool_ver == "no":

        break
