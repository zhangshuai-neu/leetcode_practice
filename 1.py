# -*- coding:utf-8 -*-
import math
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 计算dp，dp记录0,0-9,10-99..中1的的个数
        dp = [0]
        sn = str(n)
        bit_num = len(sn) # n的位数
        for i in range(bit_num):
            t = 10**i
            temp_dp = t # 首位为1
            temp_dp = temp_dp + 9*dp[i] # 其他
            dp.append(temp_dp)

        # 计算
        sum = 0
        for i in range(bit_num):
            m = (n//(10**i))%10 # 获取第i位的值
            # 计算当前位的值
            temp_sum = 0
            if m>0:
                temp_sum = temp_sum + math.ceil(10**(i-1)) # 首位为1
                temp_sum = temp_sum + m*dp[i] # 其他
                sum = sum + temp_sum
        return sum

# 测试
s = Solution()
ret = s.NumberOf1Between1AndN_Solution(1)
print(ret)
ret = s.NumberOf1Between1AndN_Solution(11)
print(ret)
ret = s.NumberOf1Between1AndN_Solution(99)
print(ret)
ret = s.NumberOf1Between1AndN_Solution(1000)
print(ret)