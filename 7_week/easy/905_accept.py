class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_index = len(A)-1   #从右向左遍历
        odd_index = 0           #从左向右遍历

        while odd_index<even_index:
            while odd_index<even_index and A[odd_index]%2 == 0:
                odd_index = odd_index+1

            while even_index>odd_index and A[even_index]%2 ==1:
                even_index = even_index-1

            if odd_index<even_index:
                t = A[even_index]
                A[even_index] = A[odd_index]
                A[odd_index]=t
        return A

#=====================
# 测试程序
#=====================
s = Solution()

s.sortArrayByParity([1,2,3,4])

s.sortArrayByParity([0.2])
        
