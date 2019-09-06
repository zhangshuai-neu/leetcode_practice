# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # {字母:计数}
        self.map = {}

    def get_key(self, elem):
        return elem[1]

    def FirstNotRepeatingChar(self, s):
        s_len = len(s)
        for i in range(s_len):
            if s[i] in self.map:
                self.map[s[i]] += 1
            else:
                self.map.update({s[i]:1})
        
        first_num_index = -1
        for i in range(s_len):
            if first_num_index == -1:
                if self.map[s[i]] == 1:
                    first_num_index = i
            else:
                break

        return first_num_index
        
s = Solution()
print(s.FirstNotRepeatingChar("asd"))