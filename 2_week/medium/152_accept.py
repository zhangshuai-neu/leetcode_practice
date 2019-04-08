class Solution:
    # 最大连续子数组乘积，与最大子数组和类似
    # 动态规划，使用下面的递推公式
    # maxProduct[i]=MAX(maxProduct[i-1]*nums[i],minProduct[i-1]*nums[i],nums[i])
    # minProduct[i]=MIN(maxProduct[i-1]*nums[i],minProduct[i-1]*nums[i],nums[i])
    # maxProduct[i]表示以nums[i]结尾的最大连续子数组乘积
    # minProduct[i]表示以nums[i]结尾的最小连续子数组乘积
    
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #创建新的list
        nums_len = len(nums)
        max_product = [nums[i] for i in range(nums_len)]
        min_product = [nums[i] for i in range(nums_len)]
        
        i=1
        while i<nums_len:
            #最大乘积
            max_product[i] = max(max_product[i-1]*nums[i], min_product[i-1]*nums[i], nums[i])
            #最小乘积
            min_product[i] = min(max_product[i-1]*nums[i], min_product[i-1]*nums[i], nums[i])
            #索引
            i=i+1
        return max(max_product)
