class Solution:
    def insert_sort(self, num_list):
        """
        :type num_list: List[int]
        :rtype: List[int]
        """
        # 插入排序，适用于数据量比较少的情况
        # 时间复杂度: O(n^2)
        # 空间复杂度: O(1)
        # 从小到大
        
        # 1.原始方法
        """
        num_list_len = len(num_list)
        for i in range(1,num_list_len):
            # 遍历已经有序的部分，查找是否存在比num_list[i]大的元素
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
        """
        
        # 2.二分查找优化
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
        
#==================
# 测试
#==================
s = Solution()
"""
in_list = [1,3,4,5,2]
"""
in_list = [100,3,4,5,200]
print( s.insert_sort(in_list) )
