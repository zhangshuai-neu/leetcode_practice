class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        原问题 => 求两个连续元素的第k大元素的问题
        
        在log(n+m)时间内找到 nums1 和 nums2的第(m+n)/2-1 和 (m+n)/2大的元素
        然后相加除2
        
        """
        #得到第k大的元素,k从1开始
        def get_k(nums1, nums2,k):
            nums1_len = len(nums1)
            nums2_len = len(nums2)
            
            #一个为空的情况
            if nums1_len==0:
                return nums2[k-1]
            if nums2_len==0:
                return nums1[k-1]
            
            if k==1:
                return min(nums1[0],nums2[0])
            
            #避免nums中元素不够
            rm_len = min(nums1_len,nums2_len)
            if rm_len > k//2:
                rm_len = k//2
            
            if nums1[rm_len-1] < nums2[rm_len-1]:
                #删除一定比第k大的元素小的一半
                return get_k(nums1[rm_len:], nums2, k-rm_len)
            else:
                return get_k(nums1, nums2[rm_len:], k-rm_len)
        
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if (nums1_len+nums2_len)%2==0:
            k = (nums1_len+nums2_len)//2
            return ( get_k(nums1,nums2,k) + get_k(nums1,nums2,k+1) )/2
        else:
            k = (nums1_len+nums2_len+1)//2
            return get_k(nums1, nums2,k)

#==============
s= Solution()
"""
nums1 = [1]
nums2 = [2,3,4,5,6,7]

nums1 = [1,3]
nums2 = [2]
"""
nums1 = [1,2]
nums2 = [3,4]
val = s.findMedianSortedArrays(nums1,nums2)
print(val)
            
                

        
