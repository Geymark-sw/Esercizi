import time
from random import randint




#funzione che prende in ingresso una lista di posizioni e la restituisce aggiornata con la posizione aggiornata della tatrtaruga
def calcola_tartaruga(lista_posizioni: list[str],posizione: int) -> dict:

    num: int = randint(1,10)
    spostamento: int = 0


    #passo veloce: avanza di 3 posizioni
    if num >= 1 and num <= 5: 

        if posizione + 3 >= len(lista_posizioni) - 1:

            lista_posizioni[len(lista_posizioni)-1] = "Tartaruga"

        elif lista_posizioni[posizione + 3] == "_":
            lista_posizioni[posizione + 3] = "Tartaruga"
            
        else:

            lista_posizioni[posizione + 3] = "OUCH"
        
        posizione += 3
        spostamento = 3
        
        
        

    #scivolata: arretra di 6 posizioni, ma non può andare sotto la posizione 1
    elif num >= 6 and num <= 7:
        
        if posizione - 6 <= 0:
            if lista_posizioni[0] == "_":
                lista_posizioni[0] = "Tartaruga"
            else:
                lista_posizioni[0] = "OUCH"
            spostamento = -posizione
            posizione = 0
            


        elif lista_posizioni[posizione - 6] == "_":
            lista_posizioni[posizione - 6] = "Tartaruga"
            posizione -= 6
            spostamento = -6
        else:
            lista_posizioni[posizione - 6] = "OUCH"
            posizione -= 6
            spostamento = -6

        

    #passo lento: avanza di 1 posizione

    
    elif posizione + 1 >= len(lista_posizioni) - 1:

            lista_posizioni[len(lista_posizioni)-1] = "Tartaruga"

    elif lista_posizioni[posizione + 1] == "_":

        lista_posizioni[posizione + 1] = "Tartaruga"
        spostamento = 1
        posizione += 1
    else:
        lista_posizioni[posizione + 1] = "OUCH"
        spostamento = 1
        posizione += 1

    #controllo posizione precedente
    if lista_posizioni[posizione - spostamento] == "OUCH":

        lista_posizioni[posizione - spostamento] = "Lepre"

    else:

        lista_posizioni[posizione - spostamento] = "_"
    


    return {"lista":lista_posizioni, "posizione":posizione}

def calcola_lepre(lista_posizioni: list[str], posizione: int) -> dict:

    num: int = randint(1,10)
    spostamento: int = 0

    #riposo
    if num >= 1 and num <= 2:
        pass
    #grande balzo: avanza di 9 quadrati
    elif num >= 3 and num <= 4:

        if posizione + 9 >= len(lista_posizioni) - 1:

            lista_posizioni[len(lista_posizioni)-1] = "Lepre"

        elif lista_posizioni[posizione + 9] == "_":
            lista_posizioni[posizione + 9] = "Lepre"
        else:
            lista_posizioni[posizione + 9] = "OUCH"
        posizione += 9
        spostamento = 9
        
    #grande scivolata: arretra di 12 posizioni ma non può andare sotto la posizione 1
    elif num == 5:

        if posizione - 12 <= 0:
            if lista_posizioni[0] == "_":
                lista_posizioni[0] = "Lepre"

            else:
                lista_posizioni[0] = "OUCH"
            
            spostamento = -posizione
            posizione = 0

        elif lista_posizioni[posizione - 12] == "_":
            lista_posizioni[posizione - 12] = "Lepre"
            posizione -= 12
            spostamento = -12
        else:
            lista_posizioni[posizione - 12] = "OUCH"
            posizione -= 12
            spostamento = -12

        
    #piccolo balzo: avanza di 1 posizione
    elif num >= 6 and num <= 8:

        if posizione + 1 >= len(lista_posizioni) - 1:

            lista_posizioni[len(lista_posizioni)-1] = "Lepre"

        if lista_posizioni[posizione + 1] == "_":
            lista_posizioni[posizione + 1] = "Lepre"
        else:
            lista_posizioni[posizione + 1] = "OUCH"
        posizione += 1
        spostamento = 1
    #piccola scivolata: arretra di 2 posizioni ma non può andare sotto la posizione 1
    else:

        if posizione - 2 <= 0:
            if lista_posizioni[0] == "_":
                lista_posizioni[0] = "Lepre"
            else:
                lista_posizioni[0] = "OUCH"
            spostamento = -posizione
            posizione = 0

        elif lista_posizioni[posizione - 2] == "_":
            lista_posizioni[posizione - 2] = "Lepre"
            

        else:
            lista_posizioni[posizione - 2] = "OUCH"

        posizione -= 2
        spostamento = -2

    #cambio lo stato della vecchia posizione

    if num >= 1 and num <= 2:#se la lepre ha riposato, deve rimanere nella sua posizione, non deve scomparire :)
        pass

    elif lista_posizioni[posizione - spostamento] == "OUCH":

        lista_posizioni[posizione - spostamento] = "Tartaruga"

    else:

        lista_posizioni[posizione - spostamento] = "_"


    return {"lista":lista_posizioni, "posizione":posizione}


lista_posizioni: list[str] = ["_" for i in range(70)]
posizione: int = 0

tartaruga: dict = {"lista":lista_posizioni,"posizione":posizione}
lepre: dict = {"lista":lista_posizioni,"posizione":posizione}



while lista_posizioni[len(lista_posizioni) - 1] == "_":

    tartaruga = calcola_tartaruga(tartaruga["lista"],tartaruga["posizione"])
    lepre["lista"] = tartaruga["lista"]
    lepre = calcola_lepre(lepre["lista"],lepre["posizione"])
    tartaruga["lista"] = lepre["lista"]

    print(lepre["lista"])
    print("\n\n")


    time.sleep(0.5)
    







            
