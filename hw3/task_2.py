from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """Сложность функции O(n*m)"""

        row, col = len(grid)-1, len(grid[0])-1
        count = 0

        def dfs(y, x):
            if grid[y][x] == 1:
                return True
            if y <= 0 or x <= 0 or y >= len(grid)-1 or x >= len(grid[0])-1:
                return False
            grid[y][x] = 1
            up = dfs(y+1, x)
            down = dfs(y-1, x)
            left = dfs(y, x+1)
            right = dfs(y, x-1)

            return all([up, down, left, right])
        for y in range(1, row+1):
            for x in range(1, col+1):
                if grid[y][x] == 0 and dfs(y, x):

                    count += 1

        return count
