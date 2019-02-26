class Solution:
    def insert_sort(self, num_list):
        # 1.二分查找优化
        def binary_find_bigger(val_list, left, right, target):
            #查找是否有比target更大的元素，如果有返回索引，没有返回-1
            if target>val_list[right]:
                return -1
            #二分查找
            #在left和right
            while left<=right:
                mid = left + (right-left)//2
                if val_list[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return left

        num_list_len = len(num_list)
        for i in range(1,num_list_len):
            # 遍历已经有序的部分，查找是否存在比num_list[i]大的元素
            index = binary_find_bigger(num_list, 0, i-1, num_list[i])
            temp_val = num_list[i]
            if index!=-1:
                k=i-1
                while k>=index:
                    num_list[k+1] = num_list[k]
                    k=k-1
                num_list[index] = temp_val
        return num_list
        
    def bucket_sort(self, num_list):
        """
        :type num_list: List[int]
        :rtype: List[int]
        """
        # 每个bucket的范围为 n ~ n+1
        # 这个范围内的浮点数都放到该bucket中
        max_int = math.ceil( max(num_list) )
        min_int = round( min(num_list) )
        bucket_num = max_int - min_int +1

        bucket_list = [ [] for i in range(bucket_num) ]
        for val in num_list:
            # round(2.1 - 1) => 1, 存放到bucket_list[1]中
            v = val - min_int
            bi = round(v) 
            bucket_list[bi].append(v)
        
        # 对每个bucket进行排序
        for i in range(bucket_num):
            self.insert_sort( bucket_list[i] )
        
        # 读取结果
        result_list = []
        for i in range(bucket_num):
            for val in bucket_list[i]:
                result_list.append(val+min_int)
                
        return result_list

#==================
# 测试
#==================
import math # 使用浮点数向上取整

s = Solution()
"""
in_list = [1,3,4,5,2]
"""
in_list = [1.1,3.2,4.5,1.2,2.2,2.3,4.7,5.6]
max_num = max(in_list)
print( s.bucket_sort(in_list) )
