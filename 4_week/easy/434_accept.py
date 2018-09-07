class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #对字符串s进行分割，分割符号或者参数为split参数
        l=s.split(" ")
        i=0
        while i < len(l):
            if l[i]!="":
                i=i+1
            else:
                l.pop(i)
        print(len(l))
        return len(l)

s = Solution()
s.countSegments("Hello, my name is John")
s.countSegments("")
s.countSegments("    ")
