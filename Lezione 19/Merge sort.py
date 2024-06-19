def mergeSort(a: list[int]) -> list[int]:

    """
    
    """

    if len(a) == 1:
        return a 

    mid_point: int = len(a) // 2

    left_list: list[int] = mergeSort(a[:mid_point])
    right_list: list[int] = mergeSort(a[mid_point:])
    result: list[int] = merge(left_list, right_list)


def merge(list_1: list[int], list_2: list[int]) -> list[int]:

    i, j = 0, 0

    result: list[int] = [None for _ in range(len(list_1 + list_2))]

    for k in range(len(result)):

        if list_1[i] > list_2[j]:

            result[k] = list_2[j]
            j+=1

            if j == len(list_2):

                return result[:k+1] + list_1[i:]
        else:

            result[k] = list_1[i]
            i+=1




            



if __name__ == "__main__":

    a: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    mergeSort(a)

