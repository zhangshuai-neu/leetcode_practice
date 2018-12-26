class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        如果允许 O(n log n) 的复杂度,那么可以先排序,可是本题要求 O(n)。
        由于序列里的元素是无序的,又要求 O(n),首先要想到用哈希表。
        用一个哈希表 unordered_map<int, bool> used 记录每个元素是否使用,对每个元素,以该
        元素为中心,往左右扩张,直到不连续为止,记录下最长的长度。
        """
        
        use_dict = {}
        for val in nums:
            if val not in use_dict:
                use_dict.update({val:0})
        
        max_count = 0
        for val in nums:
            if use_dict[val]==1:
                continue
            else:
                count = 1 #包括val自己
                left_val = val-1
                while left_val in use_dict:
                    use_dict[left_val]=1
                    count = count+1
                    left_val = left_val-1
                right_val = val+1
                while right_val in use_dict:
                    use_dict[right_val]=1
                    count = count+1
                    right_val = right_val+1
                    
                if count>max_count:
                    max_count = count
        return max_count
                
