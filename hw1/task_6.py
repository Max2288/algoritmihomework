def getKth(lo: int, hi: int, k: int) -> int:
    """Сложность данной программы O(n*log(n)).

    Args:
        lo (int): left side of list.
        hi (int): right side of list.
        k (int): kth integer.

    Returns:
        int: the kth integer.
    """
    def Collatz(n: int) -> int:
        """Считает теорему коллатца.
        
        Args:
            n (int): number whic we reduce to one.

        Returns:
            int: how many steps we needed.
        """        
        count = 0
        while(n) > 1:
            if n % 2 == 0:
                count += 1
                n //= 2
            else:
                n = 3*n + 1
                count += 1
        return count
    lst_nums = []  # список кортежей, в каждом картеже есть пара: исходное число и его количество шагов по
    # теореме Коллатца
    for i in range(lo, hi+1):
        lst_nums.append((i, Collatz(i)))
        lst_nums = sorted(lst_nums, key=lambda x: x[1]) # сортируем по количеству шагов
    return lst_nums[k-1][0]
