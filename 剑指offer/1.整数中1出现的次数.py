# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 计算dp，dp记录0,0-9,0-99..中1的的个数
        ns = str(n)
        bit_num = len(ns)
        dp = [0 for i in range(bit_num+1)] 
        dp[1] = 1
        for i in range(2,bit_num+1):
            dp[i] = 10**(i-1) + 10*dp[i-1]
        # print(dp)
        # 计算数量
        sum = 0
        for i in range(bit_num-1,-1,-1):
            # i为数字所在进制位
            m = (n//(10**i))%10
            sub_sum = 0
            if m>0:
                sub_sum = sub_sum+dp[i]
                if m==1:
                    if i==0: 
                        # 特别处理 case: 1
                        sub_sum = sub_sum + 1
                    else: 
                        sub_sum = sub_sum + n%(10**i)+1
                else: # m>1
                    sub_sum = sub_sum + (10**i)
                    sub_sum = sub_sum + (m-1)*dp[i]
            # print(m, sub_sum)
            sum = sum + sub_sum
        return sum

# 测试
s = Solution()

ret = s.NumberOf1Between1AndN_Solution(1)
print("1:", ret)

ret = s.NumberOf1Between1AndN_Solution(10)
print("10:", ret)

ret = s.NumberOf1Between1AndN_Solution(21)
print("21:", ret)

ret = s.NumberOf1Between1AndN_Solution(99)
print("99:", ret)

ret = s.NumberOf1Between1AndN_Solution(1345)
print("1345:", ret)

