class Solution:
    def findLongestChain(self, pairs):
        """Сложность функции O(n)."""
        pairs.sort()
        a = pairs.pop()[0]
        res = 1
        while pairs:
            c, d = pairs.pop()
            if d < a:
                res += 1
                a = c
        return res
