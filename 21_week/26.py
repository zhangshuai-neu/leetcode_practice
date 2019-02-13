class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #====================
        # 方法1： 超时
        # 
        # 只是简单的将后续的内容直接拷贝过来
        # 有极大的计算上的冗余
        # 例如：
        # 1,1,1,2,3
        # 1次: 1,1,2,3 null
        # 2次: 1,2,3 null null
        # 多次将后续的内容拷贝过来是很浪费时间的
        #====================
        """
        i = 0
        nums_len = len(nums)
        # 从头开始遍历
        while i<nums_len:
            j=i+1
            if j<nums_len and nums[i]==nums[j]:
                while j<nums_len:
                    nums[j-1] = nums[j]
                    j=j+1
                nums_len = nums_len-1
                # i停止在此处，进行下一次判断
                continue
            i=i+1
        
        return nums_len
        """
        
        #=============================
        # 方法2： 直接把当前数组当成两部分
        # 1,2,3,4,5,...
        #     i j
        # i 指向不重复的的数组的末尾
        # j 指向未处理的部分
        #=============================
        i = j = 0
        nums_len = len(nums)
        if nums_len ==0:
            return 0
            
        for j in range(1, nums_len):
            if i<j and nums[i]!=nums[j]:
                i = i+1
                nums[i] = nums[j]
        return i+1
        
        
#=====================
# 测试
#=====================
s = Solution()
nums=[1,1,2,2,3]
s.removeDuplicates(nums)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
