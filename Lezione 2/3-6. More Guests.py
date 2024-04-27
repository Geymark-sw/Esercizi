"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
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
