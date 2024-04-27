"""
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""

p: list[str] = ["Andrea Larosa","Abella Danger","Gaggi Yatarov"]

for i in p:
    print(f"Ciao {i}, ti andrebbe di uscire a cena?")
    
print(f"{p[2]}: Mi dispiace ma non posso venire a cena :(")

p[2] = "Emanuele Majeli"

for i in p:
    print(f"Ciao {i}, ti andrebbe di uscire a cena?")