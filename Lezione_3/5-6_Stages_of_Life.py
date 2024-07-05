ver: bool = True
ris: str

while ver:
    età: int = int(input("Inserisci l'età:"))

    if età < 2:
        print("The person is a baby")

    elif età == 2 or età < 4:
        print("The person is a toddler")
    elif età == 4 or età < 13:
        print("The person is a kid")
    elif età == 13 or età < 20:
        print("The person is teenager")
    elif età == 20 or età < 65:
        print("The person is an adult")
    elif età >= 65:
        print("The person is al elder")
    
    print("Vuoi ripetere l'operazione? Si/No")
    ris = input().lower()
    if  ris == "si":
        ver = True

    elif ris == "no" or ris != "no":
        ver = False