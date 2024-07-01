"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
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