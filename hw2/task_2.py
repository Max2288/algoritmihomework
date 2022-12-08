class Solution:
    
    def getMaximumGenerated(self, n: int) -> int:
        """Сложность данной функции O(n+1).

        Args:
            n (int): list's length.

        Returns:
            int: the maximum element in this list.
        """        
        if not n:
            return n
        #Генерируем список по условию задачи и возвращаем максимальный элемент
        nums = [0]*(n+1)
        nums[1] = 1
        for i in range(2, n+1):
            if i % 2:
                nums[i] = nums[i//2]+nums[i//2+1]
            else:
                nums[i] = nums[i//2]
        return max(nums)
    