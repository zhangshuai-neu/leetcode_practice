# -*- coding:utf-8 -*-

# 暴力的做法：n^2
class Solution:
    def InversePairs(self, data):
        data_len = len(data)
        sum = 0
        for i in range(data_len):
            for j in range(i+1, data_len):
                if data[i]>data[j]:
                    sum = sum +1
        return sum%1000000007

# 第一种做法，会超时 n^2, 也可以原址排序
class Solution1:
    def __init__(self):
        # 从a[n]向a[0]进行插入排序
        self.sort_list = []
        self.sort_list_len = 0
        # 记录data[i+1]到末尾，比data[i]小的元素个数
        self.count_list = [] 
    
    # 获取第一个更小的元素的索引
    def get_fisrt_smaller_elem_index(self, elem):
        left = 0
        right = self.sort_list_len-1
        # 在左侧 或 右侧
        if self.sort_list[left] >= elem:
            return left-1
        if self.sort_list[right] < elem:
            return right
        # 在中间
        while left < right :
            mid = left//2 + right//2
            if self.sort_list[mid] >= elem:
                right = mid-1
            else:
                left = mid+1
        if self.sort_list[min(left, right)] >= elem:
            return min(left, right)-1
        return min(left, right)

    # 将elem插入到sort_list种，并存储比elem小的元素个数
    def insert_sort(self, elem):
        if self.sort_list_len == 0:
            self.count_list.append(0)
            self.sort_list.append(elem)
            self.sort_list_len += 1
        else:
            i = self.get_fisrt_smaller_elem_index(elem)
            self.count_list.append((i+1)%1000000007)
            self.sort_list.insert(i+1, elem)
            self.sort_list_len += 1

    def InversePairs(self, data):
        # 其实就是在找后面比data[i]小的数字的个数，然后在求和
        data_reverse = data
        data_reverse.reverse()
        for elem in data_reverse:
            self.insert_sort(elem)
        return sum(self.count_list) % 1000000007

# 类似归并的做法：
class Solution2:
    def merge_sort(self, data, start, end, temp_data):
        data_len = end - start
        if data_len <= 1:
            return 0

        mid = (start + end)//2
        left_sum = self.merge_sort(data, start, mid, temp_data)
        right_sum = self.merge_sort(data, mid, end, temp_data)
        all_sum = left_sum + right_sum
        # 处理合并
        i = start
        left_i = start
        right_i = mid
        while left_i < mid and right_i < end:
            if data[right_i] < data[left_i]:
                all_sum += (mid - left_i)
                temp_data[i] = data[right_i]
                right_i += 1
                i += 1
            else:
                temp_data[i] = data[left_i]
                left_i += 1
                i += 1
        
        while left_i < mid:
            temp_data[i] = data[left_i]
            left_i += 1
            i += 1
        while right_i < end:
            temp_data[i] = data[right_i]
            right_i += 1
            i += 1
        
        # print("debug:", data[start:end], mid, left_sum, right_sum, all_sum)

        for i in range(start, end):
            data[i] = temp_data[i]
        return all_sum

    def InversePairs(self, data):
        data_len = len(data)
        temp_data = [ 0 for i in range(data_len)]
        sum = self.merge_sort(data, 0, data_len, temp_data)
        return sum%1000000007
        

# 测试
data = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,
    965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,
    576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,
    655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
# 对应输出应该为: 2519

s = Solution()
r = s.InversePairs(data)
print(r)

"""
s1 = Solution1()
r1 = s1.InversePairs(data)
print(r1)
"""

data = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,
    965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,
    576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,
    655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
s2 = Solution2()
r2 = s2.InversePairs(data)
print(r2)