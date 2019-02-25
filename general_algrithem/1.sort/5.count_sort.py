class Solution:
    def count_sort(self, num_list, max_num):
        """
        :type num_list: List[int]
        :rtype: List[int]
        """
        count_list = [ 0 for i in range(max_num+1) ]
        num_list_len = len(num_list)
        for num in num_list:
            count_list[num] = count_list[num]+1
        
        nl_i = 0 # nl_i num_list的索引
        for cl_i in range(max_num+1): 
            # cl_i count_list的索引
             while count_list[cl_i]!=0:
                count_list[cl_i] = count_list[cl_i]-1
                num_list[nl_i] = cl_i
                nl_i = nl_i +1
#==================
# 测试
#==================
s = Solution()
"""
in_list = [1,3,4,5,2]
"""
in_list = [1,3,4,5,2,10]
max_num = max(in_list)
s.count_sort(in_list, max_num)
print( in_list )
