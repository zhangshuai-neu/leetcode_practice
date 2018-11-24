class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #使用简单方法，KMP比较快
        if needle == "":
            return 0
        
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle>len_haystack:
            return -1

        # +1 避免出现"a"和"a"这种情况
        for i in range(len_haystack-len_needle+1):
            if haystack[i]==needle[0]:
                if haystack[i:i+len_needle] == needle:
                    return i
        return -1
