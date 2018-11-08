class Solution:
    def maxCoins(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        """
        max_coins = 0
        
        # n在1～3的范围内
        n = len(nums)
        if n==1:
            return nums[0]
        
        # 
        for i in range(n):
            t = nums[i]
            if i-1>=0:
                t= nums[i-1]*t
            if i+1<n:
                t= nums[i+1]*t
                
            l=nums[0:i]
            l.extend(nums[i+1:])
            temp_maxc = t + self.maxCoins(l)
            max_coins = max(temp_maxc,max_coins)
        
        return max_coins
