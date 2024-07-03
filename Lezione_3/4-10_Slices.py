primi_10_cubi: list[int] = [i**3 for i in range(1,11)]


print(f"Gli elementi della lista sono:")
for i in primi_10_cubi:
    print(i)

print(f"I primi 3 elementi della lista sono: ")
for i in primi_10_cubi[:3]:

    print(i)
    

print(f"I 3 elementi dalla metà della lista sono:")
for i in primi_10_cubi[len(primi_10_cubi)//2-1:len(primi_10_cubi)//2+2]:

    print(i)

print(f"Gli ultimi elementi della lista sono:")
for i in primi_10_cubi[-3:]:

    print(i)