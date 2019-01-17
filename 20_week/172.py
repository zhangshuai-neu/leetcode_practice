class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1) 要求末尾有多少个零，则该数应为x*10^k 的形式等于x*（2^k * 5^k）
        # 2) 偶数一定比5的数量多, 所以因式分解后5的个数等于 末尾0的个数
        count = 0 
        while n>=5:
            count = count + n//5
            n = n//5
        return count
