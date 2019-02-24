class Solution:
    def quick_sort(self, num_list, begin, end):
        """
        :type num_list: List[int]
        """
        # 快速排序
        # 4 5 1 2 3 作为例子进行思考
        if end-begin<1:
            return
            
        print(num_list, begin, end)
        partition = begin-1
        for i in range(begin,end):
            if num_list[i] < num_list[end]:
                partition = partition+1
                t = num_list[i]
                num_list[i] = num_list[partition]
                num_list[partition] = t
        
        partition = partition+1
        t = num_list[end]
        num_list[end] = num_list[partition]
        num_list[partition] = t
        
        self.insert_sort(num_list, begin, partition-1)
        self.insert_sort(num_list, partition+1, end)
#==================
# 测试
#==================
s = Solution()
"""
in_list = [1,3,4,5,2]
in_list = [100,3,4,5,200,1]
"""
in_list = [1,3,4,5,2]
s.quick_sort(in_list, 0, len(in_list)-1)
print( in_list )
