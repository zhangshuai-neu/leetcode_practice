class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_len = len(A)
        even_i = 0
        odd_i = 1
        while odd_i<A_len and even_i<A_len:
            #奇数
            while odd_i<A_len and A[odd_i]%2==1:
                odd_i = odd_i+2
            #偶数
            while even_i<A_len and A[even_i]%2==0:
                even_i = even_i+2
                
            print(odd_i, even_i)
            if even_i<A_len and odd_i<A_len:
                t = A[odd_i]
                A[odd_i] = A[even_i]
                A[even_i] = t
        return A

#========================
s = Solution()
s.sortArrayByParityII([4,2,5,7])
