class Solution:
    def insert_sort(self, num_list):
        """
        :type num_list: List[int]
        :rtype: List[int]
        """
        # 插入排序，适用于数据量比较少的情况
        # 
        # 从小到大
        num_list_len = len(num_list)
        
        for i in range(1,num_list_len):
            for j in range(0,i):
                if num_list[i]<num_list[j]:
                    temp_num = num_list[i]
                    # 将[j，i)全体后移
                    k=i-1
                    while k>=j:
                        num_list[k+1] = num_list[k]
                        k=k-1
                    num_list[j] = temp_num
        return num_list
        
#==================
# 测试
#==================
s = Solution()
"""
in_list = [1,3,4,5,2]
"""
in_list = [100,3,4,5,200,1]

print( s.insert_sort(in_list) )
