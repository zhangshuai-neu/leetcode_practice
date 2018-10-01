class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        nums.sort()
        
        min_pari_sum = 0
        for i in range(nums_len//2):
            min_pari_sum = min_pari_sum + nums[i*2]
        
        return min_pari_sum
        
#==========================
# 测试程序
#==========================
s = Solution()

s.arrayPairSum([1,4,3,2])
