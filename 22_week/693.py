class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        or_bits = 3
        while n!=0:
            if n&or_bits==3 or n&or_bits==0:
                return False
            n = n>>1
        return True

#===============
# 测试
#===============
s = Solution()

print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
