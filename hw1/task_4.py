def minimumAbsDifference(arr: list) -> list:
    """Сложность данной программы O(n*log(n)).
    
    Args:
        arr (list): an array of distinct integers.

    Returns:
        list: a list of pairs in ascending order(with respect to pairs).
    """
    arr.sort() # сортируем список стандартным методом
    min_diff = 10**6
    for i in range(1, len(arr)): # ищем минимальную разницу между элементами
        diff = arr[i]-arr[i-1]
        if diff < min_diff:
            min_diff = diff
    lst = []
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1] == min_diff: # если минимальная разница равна разности чисел добавляем в список
            lst.append([arr[i-1], arr[i]]) 
    return lst
