"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of 
people you’re inviting to dinner.
"""


p: list[str] = ["Andrea Larosa","Abella Danger","Gaggi Yatarov"]

for i in p:
    print(f"Ciao {i}, ti andrebbe di uscire a cena?")
    
print(f"{p[2]}: Mi dispiace ma non posso venire a cena :(")

p[2] = "Emanuele Majeli"

for i in p:
    print(f"Ciao {i}, ti andrebbe di uscire a cena?")

print("RAGAZZI HO TROVATO UN TAVOLO PIÙ GRANDE, PROVO AD INVITARE ALTRE 3 PERSONE")

p.insert(0,"Manuel Caruso")
p.insert(2,"Lana Rhoades")
p.append("Erik Barsi")

for i in p:
    print(f"Ciao {i}, ti andrebbe di uscire a cena?")

print("MI DISPIACE RAGAZZI MA A CAUSA DI PROBLEMI DI PRENOTAZIONE DEL TAVOLO POSSO INVITARE SOLO 2 PERSONE")

for i in range(2,len(p)):
    j: int = 2 #variabile definita per eliminare 4 elementi con indice 2 visto chge la lista è lunga 6
    print(f"Mi dispiace {p.pop(j)}, ma non sei più invitato alla cena")



for i in p:
    print(f"Ciao {i}, sei ancora invitato alla cena.")

for i in range(0,2):
    del p[0]

print(p)

print(f"Le persone invitate sono: {len(p)}")


