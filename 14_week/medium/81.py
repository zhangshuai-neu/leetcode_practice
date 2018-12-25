class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums_len = len(nums)
        
        left = 0
        right = nums_len -1
        
        while left<=right:
            mid = left + (right-left)//2
            
            if nums[mid]==target:
                return True
            
            if nums[mid]>nums[left]:
                if target>=nums[left] and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<nums[left]:
                    if target>nums[mid] and target<=nums[right]:
                        left = mid+1
                    else:
                        right = mid-1
                else:
                    #特殊情况 例如 1 1 2 3 1 1 1 1 和 1 1 1 1 2 3
                    left = left+1
        return False
                    
