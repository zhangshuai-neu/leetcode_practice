# -*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        self.map = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 8:6, 9:7, 10:8, 12:9, 15:10} # 记录的丑数和对应索引
        self.data = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
        self.len = 11
        self.prime_num = [2, 3, 5]

    # 找到data种第一个比 t大的数字
    def get_first_big_in_data(self, t):
        if t in self.map:
            return self.map[t]
        left = mid = 1
        right = self.len-1
        while left < right:
            mid = (left+right)//2
            if self.data[mid]>t:
                right = mid
            else:
                left = mid +1
        return left-1

    # 找到下一个可能的丑数
    def get_next_ugly_num_list(self, cur_ugly_num):
        result = []
        for prime_n in self.prime_num:
            factor = cur_ugly_num//prime_n
            index = self.get_first_big_in_data(factor) + 1
            new_ugly_num = self.data[index] * prime_n
            # print("factor:",factor, "index", index, "new_ugly_num",new_ugly_num)
            if index < self.len and new_ugly_num > cur_ugly_num:
                result.append(new_ugly_num)
        return result

    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        # 已经求解
        if index <= self.len:
            return self.data[index-1]
        # 尚未求解
        while self.len<= index:
            # 获取next丑数
            cur_max_ugly_num = self.data[self.len-1]
            next_ugly_num_list = self.get_next_ugly_num_list(cur_max_ugly_num)  
            next_ugly_num = min(next_ugly_num_list)
            # 更新存储
            self.data.append(next_ugly_num)
            self.map.update({next_ugly_num:self.len})
            self.len = self.len +1
        return self.data[index-1]

s = Solution()
print(s.GetUglyNumber_Solution(20))
print(s.data)
print(s.map)
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 25, 27, 30, 36, 40, 45, 50
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36