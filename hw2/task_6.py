from typing import List


class Solution:
    
    def rob(self, nums: List[int]) -> int:
        """Сложность данной функции O(n).Так как первый и последний дом связаны(по условию задачи) то написал вспомогательную функцию, которую необходимо запустить с 1 элемента или до последнего.

        Args:
            nums (List[int]): representation of houses which we should rob.

        Returns:
            int: the maximum money which we can steal.
        """        
        def checker_rob(nums):
            """Сложность данной функции O(n).

            Args:
                nums (_type_): representation of houses which we should rob.
            Returns:
                int: the maximum money which we can steal.
            """            
            rob = 0
            not_rob = 0
            for num in nums:
                rob , not_rob = not_rob + num , max(rob,not_rob)
            return max(rob,not_rob)    
        if len(nums) == 1:
            return nums[-1]
        elif not nums:
            return 0
        else:
            return max(checker_rob(nums[1:]),checker_rob(nums[:-1]))
    