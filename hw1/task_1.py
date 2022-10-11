def numberOfSteps(num: int) -> int:
    """Сложность данной программы O(n).
    
    Args:
        num (int): num which we reduce to zero.

    Returns:
        int: the number of steps to reduce it to zero.
    """
    count = 0 # счётчик шагов
    while num != 0:
        if num % 2 == 0:
            num //= 2
            count += 1
        else:
            num -= 1
            count += 1
    return count
