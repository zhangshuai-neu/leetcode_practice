class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if A==None:
            return 0
        
        count = 0
        A_len = len(A)
        str_len = len(A[0])
        for column in range(str_len):
            for i in range(A_len):
                if i+1<A_len and ord(A[i+1][column])<ord(A[i][column]):
                    count = count+1
                    break
        return count

s = Solution()
print(s.minDeletionSize(["cbao", \
                         "dafp", \
                         "ghiq"]))
        
        
