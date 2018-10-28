class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_len = len(prices)
        max_profit = 0
        
        for i in range(prices_len):
            for j in range(i+1,prices_len):
                max_profit = max(prices[j]-prices[i],max_profit)

        return max_profit
        
#=================
