"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""

p:list[str] = ["Roma", "Tokyo", "Londra", "Berlino", "Zurigo"]

print(f"Lista originale: {p}")

print(f"Lista sorted: {sorted(p)}")

print(f"Lista originale: {p}")

print(f"Lista sorted reverse: {sorted(p,reverse = True)}")

print(f"Lista originale: {p}")

p.reverse()
print(f"Lista reverse: {p}")

print(f"Lista originale: {p}")

p.reverse()
print(f"Lista reverse: {p}")

p.sort()
print(f"Lista sort: {p}")

p.sort(reverse = True)
print(f"Lista sort invertito: {p}")
print(f"Lista originale: {p}")


