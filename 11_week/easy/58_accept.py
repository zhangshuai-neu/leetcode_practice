class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sl = list(s.split())
        if len(sl)==0:
            return 0
        return len(sl[len(sl)-1])

#=================================
s = Solution()
print(s.lengthOfLastWord("hello world"))
