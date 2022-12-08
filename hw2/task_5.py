from typing import List


class Solution:
    
    def getDescentPeriods(self, prices: List[int]) -> int:
        """Сложность данной функции O(n).

        Args:
            prices (List[int]): representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

        Returns:
            int: the number of smooth descent periods.
        """        
        length = len(prices)
        dp = [1]*length
        sm = 1 #количество периодов
        for i in range(1, length):
            if prices[i-1]-prices[i] == 1:
                dp[i] = dp[i-1]+1
            sm += dp[i]
        return sm
