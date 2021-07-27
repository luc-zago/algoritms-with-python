def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_string, second_string = list(first_string), list(second_string)
    selection_sort(first_string)
    selection_sort(second_string)
    if first_string == second_string:
        return True
    return False
