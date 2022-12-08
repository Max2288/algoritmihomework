from typing import List


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        """Сложность данной функции O(n*m).

        Args:
            matrix (List[List[int]]): matrix where we search squares.

        Returns:
            int: the amount of squares in matrix.
        """
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] > 0:
                    # если элемент матрицы больше нуля то пытаемся расширить квадрат путём нахождения минимального из левого, верхнего и диагонального соседа
                    matrix[i][j] = 1+min(matrix[i][j-1],
                                         matrix[i-1][j-1], matrix[i-1][j])
        # в конце идём по матрице и считаем сумму ячеек
        s = 0
        for el in matrix:
            s += sum(el)
        return s
