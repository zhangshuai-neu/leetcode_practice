class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_len = len(prices)
        max_profit = 0
        
        if prices_len<2:
            return max_profit
        
        min_stock = prices[0]
        #顺序遍历，并记录当前值和左侧最小值
        for i in range(1,prices_len):
            min_stock = min(prices[i-1],min_stock)
            max_profit = max(prices[i]-min_stock,max_profit)
            
        return max_profit
        
#=================
