def stampa_messaggi(lista: list[str]) -> None:
    
    cont: int = 1
    for i in lista:

        print(f"Messaggio {cont}: {i}")

        cont += 1


stampa_messaggi(["ciao","come stai","Tutto Bene?"])