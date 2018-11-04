class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 考虑一下质数的问题
        # 合数要找最大的约数，因为paste的单元只能是n的约数
        
        if n==1:
            return 0
        
        # 质数标志
        prime_flag = 1
        # 判断是否为质数
        sqrt_n = int(pow(n,0.5))
        for i in range(2,sqrt_n+1):
            if n%i==0:
                prime_flag=0
                break
        
        # 由于质数不可分解，不可能用copy-paste减少步骤，返回n
        if prime_flag:
            return n
            
        # 合数，优先级别:2分,3分,4分,因为paste的单元最大
        for i in range(2,n):
            if n%i==0:
                return i+ self.minSteps(n//i)

#==============
s = Solution()
print(s.minSteps(6))
