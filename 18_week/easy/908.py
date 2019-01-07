class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_A = max(A)
        min_A = min(A)
        
        if max_A-min_A <= 2*K:
            return 0
        else:
            return max_A-min_A -2*K
