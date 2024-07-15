import time
from random import randint




#funzione che prende in ingresso una lista di posizioni e la restituisce aggiornata
def calcola_tartaruga(lista_posizioni: list[str],posizione: int) -> list[str]:

    num: int = randint(1,10)


    #passo veloce: avanza di 3 posizioni
    if num >= 1 and num <= 5: 
        if lista_posizioni[posizione + 3] == "_":
            lista_posizioni[posizione + 3] = "Tartaruga"
            
        else:

            lista_posizioni[posizione + 3] = "OUCH"
        
        

    #scivolata: arretra di 6 posizioni, ma non può andare sotto la posizione 1
    elif num >= 6 and num <= 7:
        
        if posizione - 6 <= 0:
            if lista_posizioni[0] == "_":
                lista_posizioni[0] = "Tartaruga"
            else:
                lista_posizioni[0] = "OUCH"


        elif lista_posizioni[posizione - 6] == "_":
                lista_posizioni[posizione - 6] = "Tartaruga"

        else:
            lista_posizioni[posizione - 6] = "OUCH"

        

    #passo lento: avanza di 1 posizione
    elif lista_posizioni[posizione + 1] == "_":

        lista_posizioni[posizione + 1] = "Tartaruga"
    else:
        lista_posizioni[posizione + 1] = "OUCH"
    
    lista_posizioni[posizione] = "_"


    return lista_posizioni

def calcola_lepre(lista_posizioni: list[str], posizione: int) -> list[str]:

    num: int = randint(1,10)

    #riposo
    if num >= 1 and num <= 2:
        pass
    #grande balzo: avanza di 9 quadrati
    elif num >= 3 and num <= 4:
        if lista_posizioni[posizione + 9] == "_":
            lista_posizioni[posizione + 9] = "Lepre"
        else:
            lista_posizioni[posizione + 9] = "OUCH"
    #grande scivolata: arretra di 12 posizioni ma non può andare sotto la posizione 1
    elif num == 5:

        if posizione - 12 <= 0:
            if lista_posizioni[0] == "_":
                lista_posizioni[0] = "Lepre"

            else:
                lista_posizioni[0] = "OUCH"

        elif lista_posizioni[posizione - 12] == "_":
            lista_posizioni[posizione - 12] = "Lepre"
        else:
            lista_posizioni[posizione - 12] = "OUCH"
    #piccolo balzo: avanza di 1 posizione
    elif num >= 6 and num <= 8:

        if lista_posizioni[posizione + 1] == "_":
            lista_posizioni[posizione + 1] = "Lepre"
        else:
            lista_posizioni[posizione + 1] = "OUCH"
    #piccola scivolata: arretra di 2 posizioni ma non può andare sotto la posizione 1
    else:

        if posizione - 2 <= 0:
            if lista_posizioni[0] == "_":
                lista_posizioni[0] = "Lepre"
            else:
                lista_posizioni[0] = "OUCH"

        elif lista_posizioni[posizione - 2] == "_":
            lista_posizioni[posizione - 2] = "Lepre"

        else:
            lista_posizioni[posizione - 2] = "OUCH"

    lista_posizioni[posizione] = "_"


    return lista_posizioni


lista_posizioni: list[str] = ["_" for i in range(70)]

for i in range(len(lista_posizioni)):

    lista_posizioni = calcola_tartaruga(lista_posizioni,i)
    lista_posizioni = calcola_lepre(lista_posizioni,i)

    print(lista_posizioni)

    time.sleep(0.5)
    







            
