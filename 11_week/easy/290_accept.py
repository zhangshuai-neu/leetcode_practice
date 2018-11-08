class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = list(str.split())
        pattern_len = len(pattern)
        
        # 长度不同
        if pattern_len != len(str_list):
            return False
        
        # 词典
        pattern_dict = {}
        str_dict = {}
        for i in range(pattern_len):
            if pattern[i] not in pattern_dict and str_list[i] not in str_dict: 
                pattern_dict.update({pattern[i]:str_list[i]})
                str_dict.update({str_list[i]:pattern[i]})
            else:
                if pattern[i] in pattern_dict and pattern_dict[pattern[i]]!=str_list[i]:
                    return False
                if str_list[i] in str_dict and str_dict[str_list[i]]!=pattern[i]:
                    return False
        
        return True
