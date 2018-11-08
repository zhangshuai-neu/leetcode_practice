class Solution:
    def maxCoins(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        """
        # 方法说明
        # 迭代式： 
        # maxcoins(i,j) = nums[i]*nums[k]*nums[j] + maxcoins(i,k) + maxcoins(k,j)
        # k是最后删除的一个气球，maxcoins是nums[i...j]能戳破气球的最大值
        # maxcoins(i,k)表示i,k之间的气球被删除
        # maxcoins(k,j)表示k,j之间的气球被删除
        # 由于i,k之间和k,j之间的气球被删除，所以nums[k]只能与更外围的数字相乘(nums[i]*nums[k]*nums[j])
        # maxcoins用dp替代
        # 
        # 按照 j-i == 2,3,4,5 的顺序计算
        # 参考：https://blog.csdn.net/zly9923218/article/details/51059664
        
        # 首尾添加1
        nums_len = len(nums)
        nums.insert(0,1)
        nums.append(1)
        
        n = nums_len+2
        dp = []
        for i in range(n):
            temp_list = [0 for j in range(n)]
            dp.append(temp_list)
        
        for i in range(n-2):
            dp[i][i+2] = nums[i]*nums[i+1]*nums[i+2]
        
        for l in range(3,n):
            for i in range(0,n-l):
                j = i+l
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j] )
        
        return dp[0][n-1]
