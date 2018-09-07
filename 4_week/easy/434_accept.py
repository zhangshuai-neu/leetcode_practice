class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
<<<<<<< HEAD
        #对字符串s进行分割，分割符号或者参数为split参数
        l=s.split(" ")
=======
        l=s.split(" ")
        #去掉空指令
>>>>>>> 4b6d5d2913abfb395bbc2ffcdd40abb55669b648
        i=0
        while i < len(l):
            if l[i]!="":
                i=i+1
            else:
                l.pop(i)
<<<<<<< HEAD
        print(len(l))
        return len(l)

s = Solution()
s.countSegments("Hello, my name is John")
s.countSegments("")
s.countSegments("    ")
=======
        return len(l)
>>>>>>> 4b6d5d2913abfb395bbc2ffcdd40abb55669b648
