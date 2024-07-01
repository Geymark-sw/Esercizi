"""
Scrivi una funzione che verifica se in una stringa 
le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi 
che apre c'è la corrispondente parentesi che chiude.
"""

def check_parentheses(expression: str) -> bool:
    
    apri: int = 0
    chiudi: int = 0

    for i in expression:
        if i == "(":
            apri += 1
        else:####
            chiudi += 1
            if chiudi > apri:
                return False


    if apri == chiudi and expression[0] == "(":
        return True
    else:
        return False