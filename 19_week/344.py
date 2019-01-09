class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=list(s)
        l.reverse()
        return "".join(l)
