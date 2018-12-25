class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # o(n)复杂度
        """
        nums_len = len(nums)
        for i in range(nums_len):
            if target==nums[i]:
                return i
        
        return -1
        """
        
        # o(logn)
        last = len(nums)-1
        first = 0
        while first<=last:
            
            mid = first + (last-first)//2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid]<nums[first]:
                if target>nums[mid] and target<=nums[last]:
                    first = mid+1
                else:
                    last = mid-1
            else:
                if target<nums[mid] and target>=nums[first]:
                    last = mid-1
                else:
                    first = mid+1
            
        return -1
