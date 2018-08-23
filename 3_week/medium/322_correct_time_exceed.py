class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #暴力,正确，但是在某些情况下会超时
        #动态规划，返回指定tail下的需要的最小coins数量
        def dp(sorted_coins,tail,left_amount):        
            tail_count_list = []
            if left_amount%sorted_coins[tail]==0:                
                #tail == 0也在此处进行了处理
                #tail币值即可结束
                tail_count = left_amount // sorted_coins[tail]
                tail_count_list.append(tail_count)
            else:
                if tail>0:
                    #需要该tail币值
                    max_tail_count = left_amount // sorted_coins[tail]
                    i = max_tail_count
                    while i>=0:
                        #在tail币值数量不同的情况下，进行下次递归
                        next_count = dp(sorted_coins,tail-1,left_amount-i*sorted_coins[tail])
                        #记录所有可能
                        if next_count!=-1:
                            tail_count_list.append(next_count + i)
                        i=i-1                        
            
            if len(tail_count_list)>0:
                return min(tail_count_list)
            else:
                return -1
            
                
        #比amount小的最大值的索引
        sorted_coins=sorted(coins)
        i = len(sorted_coins)-1
        while i>0 and sorted_coins[i]>amount:
            i=i-1
        tail = i    
        

        #动态规划
        min_coins=dp(sorted_coins,tail,amount)
        print(min_coins)
        
        return min_coins
        
s = Solution()
s.coinChange([1,3,5],9)
s.coinChange([346,29,395,188,155,109],9401)
