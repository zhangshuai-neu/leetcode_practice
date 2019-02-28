class Solution:
    def select_sort(self, num_list):
        """
        :type num_list: List[int]
        :rtype: List[int]
        """
        def swap(in_list, i, j):
            t = in_list[i]
            in_list[i] = in_list[j]
            in_list[j] = t
        
        nl_len = len(num_list)
        for i in range(nl_len-1):
            min_i = i
            for j in range(i,nl_len):
                if num_list[j] < num_list[min_i]:
                    min_i = j
            swap(num_list,i, min_i)

#==================
s = Solution()
"""
in_list = [1,3,4,5,2]
"""
in_list = [1,3,4,5,2]
s.select_sort(in_list)
print( in_list )

