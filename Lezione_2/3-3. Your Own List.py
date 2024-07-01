"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
"""

marche: list = ["Honda","Ferrari","Koenigsegg"]

for i in marche:
    if i == "Honda":
        print(f"Mi piace la {i} civic con il vtec")

    if i == "Ferrari":
        print(f"Mi piace il design di {i}")

    if i == "Koenigsegg":
        print(f"Mi piace l'ingegneria di {i}")