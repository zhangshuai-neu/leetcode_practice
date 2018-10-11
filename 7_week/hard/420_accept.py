class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1) 6～20个字符
        # 2) 至少一个小写字母，一个大写字母，一个数字
        # 3) 不包含三个相同字母
        char_dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dict_len = len(char_dict)
        dict_map = {}
        for i in range(dict_len):
            dict_map.update({char_dict[i]:i})
        dict_list = [0 for i in range(dict_len)]
        
        # confirm 1 
        s_len = len(s)
        if s_len>=6 or s_len<=20:
            # confirm 2
            for si in range(s_len):
                li = dict_map[s[si]]
                
        else:
            # recorrect 1
                
            
                
            
            
            
            
            
