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

autor: str = "David Goggins"

quote: str = "I don't give up when I'm tired, I give up when I'm finish"

print(f"David Goggins once said,{quote}")