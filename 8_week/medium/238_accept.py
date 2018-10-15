class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        #创建left
        left  = []
        product = 1
        for i in range(nums_len):
            product = product*nums[i]
            left.append(product)
        #创建right
        right = []
        product = 1
        j = nums_len-1
        while j>-1:
            product = nums[j]*product
            right.insert(0,product)
            j=j-1
        #计算
        result = []
        for i in range(nums_len):
            result.append(1)
            if i-1>=0:
                result[i] = result[i]*left[i-1]
            if i+1<nums_len:
                result[i] = result[i]*right[i+1]
        return result

#=====================
# 测试代码
#=====================
s = Solution()
s.productExceptSelf([1,2,3,4])
s.productExceptSelf([0,0])
