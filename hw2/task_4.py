from typing import List


class Solution:
    
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """Сложность данной функции O(n).

        Args:
            values (List[int]): integer array values where values[i] represents the value of the ith sightseeing spot.

        Returns:
            int: the maximum score of a pair of sightseeing spots.
        """        
        max_v = 0
        cur = 0
        for i in range(1, len(values)):
            cur = max(cur, values[i-1]+i-1)
            max_v = max(max_v, cur+values[i]-i)
        return max_v
