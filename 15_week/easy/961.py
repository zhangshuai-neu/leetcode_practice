class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        two_N = len(A)
        N = two_N//2
        repeat_dict = {}
        for i in range(two_N):
            if A[i] not in repeat_dict:
                repeat_dict.update({A[i]:1})
            else:
                repeat_dict[A[i]] = repeat_dict[A[i]] +1
            
            if repeat_dict[A[i]] == N:
                return A[i]
        
