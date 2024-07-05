numeri_da_1_a_9: list[int] = [i for i in range(1,10)]

for i in numeri_da_1_a_9:

    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")