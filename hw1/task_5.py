import heapq


def findKthLargest(nums: list, k: int) -> int:
    """Сложность данной программы O(n * log(k)), что равно O(n).
    
    Args:
        nums (list): an integer list with numbers.
        k (int): kth largest element.

    Returns:
        int: the kth largest element in the array.
    """
    q = heapq.nlargest(k, nums)
    return q[-1]
