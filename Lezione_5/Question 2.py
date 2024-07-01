def calculate_average(numbers: list[int]) -> float:

    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return 0
#