def is_palindrome_recursive(word, low=0, high=0):
    """Faça o código aqui."""
    if not word:
        return False
    elif len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    return is_palindrome_recursive(word[1:-1])
