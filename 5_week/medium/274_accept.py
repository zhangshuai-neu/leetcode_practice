class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        length = len(citations)
        h=0
        while h<length and citations[h]>h:
            h=h+1
        
        print(h)
        return h

#----------------------------------------
#  测试代码
#----------------------------------------
s = Solution()

s.hIndex([0])

s.hIndex([1,1])

s.hIndex([3,0,6,1,5])
