class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 动态规划表达式,空间换时间
        # dp[amount] = min(dp[amount],dp(amount-coins)+1)
        int_max = amount+1
        dp_list=[int_max for i in range(amount+1)]
        
        def dp(dp_list,)
        
        
        
        
        return dp(amount,coins)
        
s = Solution()
s.coinChange([1,3,5],9)
s.coinChange([346,29,395,188,155,109],9401)
