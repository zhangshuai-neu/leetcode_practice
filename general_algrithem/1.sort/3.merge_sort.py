class Solution:
    def merge_sort(self, num_list, temp_list, begin, end):
        # 归并排序, begin,end都是起始、结束索引
        if begin >= end:
            return
        mid = begin + (end-begin)//2
        self.merge_sort(num_list, temp_list, begin, mid)
        self.merge_sort(num_list, temp_list, mid+1, end)
        # 归并 存放到 temp_list
        i1 = begin
        i2 = mid+1
        i = begin
        while i1<=mid and i2<=end:
            if num_list[i1]<num_list[i2]:
                temp_list[i] = num_list[i1]
                i1 = i1+1
            else:
                temp_list[i] = num_list[i2]
                i2 = i2+1
            i = i+1
        while i1<=mid:
            temp_list[i] = num_list[i1]
            i1 = i1+1
            i = i+1
        while i2<=end:
            temp_list[i] = num_list[i2]
            i2 = i2+1
            i = i+1
        # temp_list -> num_list
        for i in range(begin, end+1):
            num_list[i] = temp_list[i]
        
        
#============
# 测试
#============
s = Solution()
in_list = [100,3,4,5,200]
t_list = [0,0,0,0,0]
s.merge_sort(in_list, t_list,0 , len(in_list)-1)
print(in_list)
