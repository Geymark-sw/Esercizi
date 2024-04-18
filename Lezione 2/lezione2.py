"""
2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

"""

name: str = "Geymark"

message: str = f"Ciao {name}, ti va di imparare un po' di python insieme?"

print("Hello world")

print(message)

"""2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case."""

print(f"{name}, {name.upper()}, {name.lower()}")

"""2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: 
Albert Einstein once said, “A person who never made a mistake never tried anything new.”"""

print("David Goggins once said, I don't give up when I'm tired, I give up when I'm finish")

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
 Then compose your message and represent it with a new variable called message. Print your message. 
"""

autor: str = "David Goggins"

quote: str = "I don't give up when I'm tired, I give up when I'm finish"

print(f"David Goggins once said,{quote}")


"""
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
 Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""

file_name: str = "python_notes.txt"

print(file_name.removesuffix(".txt"))

"""
3-1. Names: Store the names of a few of your friends in a list called names.
 Print each person’s name by accessing each element in the list, one at a time.
"""

names: list = ["Gey", "Ronan", "Giuse"]

for i in names:
    print(i)

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
 The text of each message should be the same, but each message should be personalized with the person’s name.
"""

for i in range(len(names)):
    if i == 0:
        print(f"Bella {names[i]}")

    if i == 1:
        print(f"Sei n cojone {names[i]}")

    if i == 2:
        print(f"Sei popo gay {names[i]}")


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

"""3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner."""



