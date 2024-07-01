"""
Scrivi una funzione che conta e ritorna quante volte un 
elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se 
non è affiancato sia a destra che a sinistra da elementi uguali.
"""

def count_isolated(numeri: list[int]) -> int:

    conta: int = 0

    if len(numeri) == 0:
         return conta
    elif len(numeri) == 1:
        return conta + 1

    if numeri[0] != numeri[1]:
        conta += 1

    if numeri[-1] != numeri[-2]:
        conta += 1

    for i in range(1,len(numeri)-1):
        
        if numeri[i] != numeri[i-1] and numeri[i] != numeri[i+1]:
            conta += 1

    

    return conta