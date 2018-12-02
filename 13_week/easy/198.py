class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1 accept
        """
        对2的改进，空间换时间，记录中间的工作过程
        
        采用递推式：
        dp[i] 表示[0,i]闭区间，随意选择情况下，rob的最大值
        dp[i] = max( dp[i-2]+nums[i] , dp[i-3]+nums[i-1] )
        参考方法2比较容易理解该递推式
        
        初始值：
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        dp[2] = max(nums[0]+nums[2],nums[1])
        dp[3]用递推式计算
        """
        nums_len = len(nums)
        dp = [0 for i in range(nums_len)]
        
        # 特殊情况
        if nums_len==0:
            return 0
        if nums_len==1:
            return nums[0]
        if nums_len==2:
            return max(nums[0],nums[1])
        if nums_len==3:
            return max(nums[0]+nums[2],nums[1])
        #假设nums长度大于3
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        dp[2] = max(nums[0]+nums[2],nums[1])
        for i in range(3,nums_len):
            dp[i] = max( dp[i-2]+nums[i] , dp[i-3]+nums[i-1] )
        return dp[nums_len-1]
        
        # 2 比较慢，超时 ================
        """
         比3好,递归比较慢，中间有冗余计算
         冗余例子：
         a, d...
         b, d...
         d之后的计算被重复了一遍
        """
        """
        方法说明：
        假设队列为： a b c d e f g h i ...
            必须要选择a,b之中的一个
            假设从c等开始向后盗窃，最后盗取的金钱是最大的
            反例： 加上a变得最大
            假设从d等开始向后盗窃，最后盗取的金钱是最大的
            反例： 加上max(a,b)变成最大
            
            迭代方法：选择a或者b之后，对新nums继续执行该策略
        """
        """
        def get_max(nums):
            nums_len = len(nums)
            if nums_len==0:
                return 0
            if nums_len==1:
                return nums[0]
            if nums_len==2:
                return max(nums)
            if nums_len==3:
                return max(nums[1],nums[0]+nums[2])
            
            max_a = 0
            max_b = 0
            max_a = nums[0] + get_max(nums[2:]) 
            max_b = nums[1] + get_max(nums[3:])
            
            return max(max_a,max_b)
        
        return get_max(nums)
        """
        
        # 3 太慢，超时 ================
        # 完全的遍历
        """
        def get_max(nums):
            nums_len = len(nums)
            if nums_len==0:
                return 0
            if nums_len==1:
                return nums[0]
            if nums_len==2:
                return max(nums)
            
            max_num = 0
            for i in range(nums_len):
                max_left = 0
                max_right = 0
                if i>1:
                    max_left = get_max(nums[0:i-1])
                if i<nums_len-2:
                    max_right = get_max(nums[i+2:])
                    
                temp_num = max_left+max_right+nums[i]
                if  temp_num > max_num:
                    max_num = temp_num
            
            return max_num
        
        return get_max(nums)
        """
#----------------------
s = Solution()
print(s.rob([155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]))

