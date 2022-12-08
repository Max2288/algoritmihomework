from typing import List


class Solution:
    def numEnclaves(grid: List[List[int]]) -> int:
        """Cложность O(n)."""
        stack = {(0, 0)}
        for i in range(len(grid)):
            stack.add((i, 0))
            stack.add((i, len(grid[i])-1))
        for i in range(len(grid[0])):
            stack.add((len(grid)-1, i))
            stack.add((0, i))
        #Два цикла добавляют края матрицы в стек
        #Если это край зануляем его и проверяем соседей если они тоже единицы, то 
        # зануляем и их
        while stack:
            i, j = stack.pop()
            if grid[i][j] == 1:
                grid[i][j] = 0
                if len(grid) > i+1:
                    stack.add((i+1, j))
                if len(grid[i]) > j+1:
                    stack.add((i, j+1))
                if 0 <= i-1:
                    stack.add((i-1, j))
                if 0 <= j-1:
                    stack.add((i, j-1))
        su = 0
        for i in grid:
            su += sum(i)
        return su
