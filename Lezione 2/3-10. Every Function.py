"""
3-10. Every Function: Think of things you could store in a list. For example, you could 
make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

lista: list[str] = ["remove suffix.txt", "txt.remove prefix","pop", "del"]

print(f"Lista originale: {lista}")



lista.insert(2, "Insert")
print(f"Insert: {lista}")
lista.append("append")
print(f"append: {lista}")
lista.pop(3)
print(f"pop: {lista}")
del lista[3]
print(f"del: {lista}")

print(f"Lista ordinata con sorted: {sorted(lista)}")
print(f"Lista sorted reverse = True {sorted(lista, reverse = True)}")

lista.sort()
print(f"sort: {lista}")
lista.sort(reverse = True)
print(f"sort revere = True: {lista}")
print(f"len: {len(lista)}")


