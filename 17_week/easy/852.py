class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #遍历
        """
        A_len = len(A)
        i=0
        while i<A_len:
            if i+1<A_len and A[i]<A[i+1]:
                i=i+1
            else:
                break
        return i
        """
        # 二分查找
        A_len = len(A)
        left = 0
        right = A_len-1
        while left<right:
            mid = left + (right-left)//2
            if ( mid-1>=0 and A[mid]>A[mid-1] ) and (mid+1<A_len and A[mid]>A[mid+1]):
                return mid
            
            if ( mid-1>=0 and A[mid-1]>A[mid] ) and ( mid+1<A_len and A[mid]>A[mid+1] ):
                right = mid
            
            if ( mid-1>=0 and A[mid-1]<A[mid] ) and ( mid+1<A_len and A[mid]<A[mid+1] ):
                left = mid+1
        return mid
