class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 递推表达式,空间换时间，dp[amount] 为amount需要的最小的coins数
        # dp[amount] = min(dp[amount],dp(amount-coins)+1)
        
        dp_list=[amount+1 for i in range(amount+1)]
        dp_list[0]=0
        #length必须提前求出，否则还是超时
        coins_len=len(coins) 
        for i in range(amount+1):
            for j in range(coins_len):
                if i>=coins[j]:
                    dp_list[i]=min(dp_list[i],dp_list[i-coins[j]]+1)
        
        print(dp_list[amount])
        
        if dp_list[amount]==amount+1:
            return -1
        return dp_list[amount]
        
#例子
s = Solution()
s.coinChange([1,3,5],9)
s.coinChange([346,29,395,188,155,109],9401)
s.coinChange([139,442,147,461,244,225,28,378,371],9914)
