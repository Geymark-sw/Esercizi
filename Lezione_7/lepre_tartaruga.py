import time
from random import randint

"""Implementare OUCH fu"""


#funzione che prende in ingresso una lista di posizioni e la restituisce aggiornata
def calcola_tartaruga(lista_posizioni: list[str],posizione: int) -> list[str]:

    num: int = randint(1,10)


    #passo veloce: avanza di 3 posizioni
    if num >= 1 and num <= 5: 
        if lista_posizioni[posizione + 3] == "_":
            lista_posizioni[posizione + 3] = "T"
            
        else:

            lista_posizioni[posizione + 3] = "OUCH"
        
        lista_posizioni[posizione] = "_"

    #scivolata: arretra di 6 posizioni, ma non può andare sotto la posizione 1
    elif num >= 6 and num <= 7:
        
        if posizione - 6 <= 1:
            
            lista_posizioni[0] = "T"

        else:

            lista_posizioni[posizione - 6] = "T"

        lista_posizioni[posizione] = "_"

    #passo lento: avanza di 1 posizione
    else:

        lista_posizioni[posizione + 1] = "T"
        lista_posizioni[posizione] = "_"


    return lista_posizioni

def calcola_lepre(lista_posizioni: list[str], posizione: int) -> list[str]:

    num: int = randint(1,10)

    #riposo
    if num >= 1 and num <= 2:
        pass
    #grande balzo: avanza di 9 quadrati
    elif num >= 3 and num <= 4:

        lista_posizioni[posizione + 9] = 

