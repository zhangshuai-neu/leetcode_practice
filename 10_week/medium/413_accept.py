class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 统计可计算切片数量
        # 0 <= P < Q < N
        # A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic
        # P + 1 < Q 至少有三个元素
        N = len(A)
        
        
        
