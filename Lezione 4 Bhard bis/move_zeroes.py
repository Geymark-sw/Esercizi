def move_zeroes(nums: list[int]) -> list:

    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))

    return nums





l: list[int] = []

while(True):
    l.append(int(input("Inserisci un numero:")))

    ver: str = input("Vuoi inserire un nuovo numero nella lista? si/no ")

    if ver.lower() != "si":
        print(l)
        print(move_zeroes(l))
        break
