def find_duplicate(nums):
    """Faça o código aqui."""
    for num in nums:
        if type(num) == str or num < 0:
            return False
        elif nums.count(num) > 1:
            return num
    return False
