class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #从比amount小的币值中选择最大的减去
        #剩余的部分存放在left_count中
        sort_coins=sorted(coins)
        index = len(coins)-1    #索引记录
        left_count = amount     #剩余部分
        coins_count = 0         #记录coins的最少使用数
        
        #从尾开始，第一个比amount小的索引
        while sort_coins[index] >amount:
            index = index -1
        
        #
        while index>=0:
            if left_count==0:
                return True
            else:
                
        
        return -1
            
        
        
