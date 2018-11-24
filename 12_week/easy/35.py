class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        
        # 特殊情况，过大或者过小
        if target>nums[right]:
            return right+1
            
        if target<nums[left]:
            return 0
            
        # 二分查找
        while left<right:
            mid = left//2 + right//2
            
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid+1
            else:
                right = mid
        return right
        
