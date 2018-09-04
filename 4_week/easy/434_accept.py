class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split(" ")
        #去掉空指令
        i=0
        while i < len(l):
            if l[i]!="":
                i=i+1
            else:
                l.pop(i)
        return len(l)
