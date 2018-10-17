class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        sort3_list = []
        nums_len = len(nums)
        for i in range(nums_len):
            num=nums[i]
            if num not in nums_dict:
                nums_dict.update({num:1})
                sort3_list.append(num)
                sort3_list.sort(reverse=True)
                if len(sort3_list)>3:
                    sort3_list.pop()
        
        if len(nums_dict)>=3:
            print(sort3_list[2])
            return sort3_list[2]
        else:
            print(sort3_list[0])
            return sort3_list[0]

#==========================
# 
#==========================

s = Solution()
s.thirdMax([3, 2, 1])

s.thirdMax([1, 2])

s.thirdMax([1,2,2,5,3,5])
