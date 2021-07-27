def quick_sort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = quick_sort([x for x in inlist[1:] if x < pivot])
        greater = quick_sort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_string, second_string = quick_sort(list(first_string)), quick_sort(
        list(second_string)
    )
    if first_string == second_string:
        return True
    return False
