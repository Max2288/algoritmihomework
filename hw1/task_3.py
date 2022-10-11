def numJewelsInStones(jewels: str, stones: str) -> int:
    """Сложность данной программы O(n).
    
    Args:
        jewels (str): jewels representing the types of stones that are jewels.
        stones (str): the stones you have.
    Returns:
        int: how many of the stones you have are also jewels.
    """
    dct = {}  # создаем словарь в котором под ключом будет каждая буква из подстроки а значением количество
    # этих букв в строке
    for letter in stones:
        if letter in dct and letter in jewels:
            dct[letter] += 1
        elif letter not in dct and letter in jewels:
            dct[letter] = 1
    return sum(dct.values())
