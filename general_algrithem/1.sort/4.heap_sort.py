class Solution:
    def heapfy(self, num_list):
        num_list_len = len(num_list)
        mid = num_list_len//2
        i = mid # i从1开始
        while i>0:
            # 从1开始计数
            # left一定存在，因为 mid==left//2, mid==right//2
            left = i*2; right = i*2+1
            if right<=num_list_len:
                if num_list[left-1] > num_list[right-1]:
                    if num_list[left-1] > num_list[i-1]:
                        t= num_list[i-1]
                        num_list[i-1] = num_list[left-1]
                        num_list[left-1] = t
                else:
                    if num_list[right-1] > num_list[i-1]:
                        t= num_list[i-1]
                        num_list[i-1] = num_list[right-1]
                        num_list[right-1] = t
            else:
                if num_list[left-1] > num_list[i-1]:
                    t= num_list[i-1]
                    num_list[i-1] = num_list[left-1]
                    num_list[left-1] = t
            i=i-1
    
    def heap_down(self, num_list, list_len):
        mid = list_len//2
        i = 1
        left = i*2; right = i*2+1
        pre_i = 0
        while i<=mid and pre_i!=i:
            pre_i = i
            if right<=list_len:
                if num_list[left-1] > num_list[right-1]:
                    if num_list[left-1] > num_list[i-1]:
                        t= num_list[i-1]
                        num_list[i-1] = num_list[left-1]
                        num_list[left-1] = t
                        i = left
                else:
                    if num_list[right-1] > num_list[i-1]:
                        t= num_list[i-1]
                        num_list[i-1] = num_list[right-1]
                        num_list[right-1] = t
                        i = right
            else:
                if num_list[left-1] > num_list[i-1]:
                    t= num_list[i-1]
                    num_list[i-1] = num_list[left-1]
                    num_list[left-1] = t
                    i = left
            left = i*2; right = i*2+1
 
    def heap_sort(self, num_list):
        # 堆排序, 原址排序
        # 1.建最大堆
        num_list_len = len(num_list)
        if num_list_len <2:
            return
        self.heapfy(num_list)
        # 2.排序
        while num_list_len>1:
            # 将最大值移到末尾
            t= num_list[0]
            num_list[0] = num_list[num_list_len-1]
            num_list[num_list_len-1] = t
            num_list_len = num_list_len-1
            #只剩一个元素，直接结束
            if num_list_len==1:
                break
            # 下沉操作
            self.heap_down(num_list, num_list_len)
            
#============
# 测试
#============
s = Solution()
in_list = [100,3,4,5,200]
in_list = [1,3,4,5,2]
s.heap_sort(in_list)
print(in_list)
