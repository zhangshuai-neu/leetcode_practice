class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_len = len(nums)
        i=0
        while i<nums_len:
            if nums[i]==val:
                nums_len = nums_len-1
                nums.pop(i)
                continue
            
            i=i+1
            
        return nums_len

#====================
s = Solution()
nums = [3,2,2,3]
val = 2
s.removeElement(nums, val)
print(nums)
