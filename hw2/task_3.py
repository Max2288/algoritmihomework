from typing import List


class Solution:
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:  
        """Сложность данной функции O((n+1)*(m+1)).

        Args:
            obstacleGrid (List[List[int]]): grid which we should research.

        Returns:
            int: he number of possible unique paths that the robot can take to reach the bottom-right corner.
        """                    
        len_row, len_col = len(obstacleGrid), len(obstacleGrid[0])        
        dp=[[0] * (len_col+1) for _ in range(len_row+1)]        
        dp[0][1]=1
        for row in range(1, len_row+1):
            for col in range(1, len_col+1):
                if not obstacleGrid[row-1][col-1]: #если встречаем 0 то заменяем его на сумму всех предыдущих шагов
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]