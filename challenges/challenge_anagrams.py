def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_string, second_string = list(first_string), list(second_string)
    insertion_sort(first_string)
    insertion_sort(second_string)
    if first_string == second_string:
        return True
    return False
