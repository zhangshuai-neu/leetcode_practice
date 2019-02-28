class Solution:
    # 希尔排序
    def group_sort(self, num_list, start_index, group_len, list_len):
        for i in range(start_index+group_len, list_len, group_len):
            # j 为比num_list[i]大的第一个元素
            for j in range(start_index, i+1, group_len):
                if  num_list[j]>num_list[i]:
                    break
            # 保存 num_list[i]
            t = num_list[i]
            # 比num_list[i]大的后移
            for k in range(i, j, -group_len):
                num_list[k] = num_list[k-group_len]
            num_list[j] = t
            
    def shell_sort(self, num_list):
        """
        :type num_list: List[int]
        :rtype: List[int]
        """
        nl_len = len(num_list)
        group_len = nl_len//2
        while group_len>0:
            for group_start in range(group_len):
                self.group_sort(num_list, group_start, group_len, nl_len)
            group_len = group_len//2
#==================
s = Solution()
in_list = [8,9,1,7,2,3,5,4,6,0]
s.shell_sort(in_list)
print( in_list )

