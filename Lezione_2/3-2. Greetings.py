"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
 The text of each message should be the same, but each message should be personalized with the person’s name.
"""

names: list = ["Gey", "Ronan", "Giuse"]

for i in range(len(names)):
    if i == 0:
        print(f"Bella {names[i]}")

    if i == 1:
        print(f"Sei n cojone {names[i]}")

    if i == 2:
        print(f"Sei popo gay {names[i]}")