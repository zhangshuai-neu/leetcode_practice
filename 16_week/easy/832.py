class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        for i in range(n):
            # 交换位置
            for j in range(n//2):
                t = A[i][j]
                A[i][j] = A[i][n-j-1]
                A[i][n-j-1] = t
            # 取反
            for l in range(n):
                if A[i][l]==1:
                    A[i][l]=0
                else:
                    A[i][l]=1
        return A
