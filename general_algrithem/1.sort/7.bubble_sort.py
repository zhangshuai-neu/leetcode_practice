class Solution:
    def bubble_sort(self, num_list):
        """
        :type num_list: List[int]
        :rtype: List[int]
        """
        def swap(in_list, i, j):
            t = in_list[i]
            in_list[i] = in_list[j]
            in_list[j] = t
        
        nl_len = len(num_list)
        for i in range(nl_len):
            for j in range(0,nl_len-1-i):
                # 将更大的向后移动
                if num_list[j]>num_list[j+1]:
                    swap(num_list, j, j+1)
        
#==================
# 测试
#==================
# 使用浮点数向上取整
import math 
s = Solution()
"""
in_list = [1,3,4,5,2]
"""
in_list = [1,3,4,5,2]
s.bubble_sort(in_list)
print( in_list )
