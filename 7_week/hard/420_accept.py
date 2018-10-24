class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1) 6～20个字符
        # 2) 至少一个小写字母，一个大写字母，一个数字
        # 3) 不包含三个连续相同字母
        # 如果不合法，给出最小的修改步骤
        char_dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char_map = {}
        for i in range(62):
        	char_map.update({char_dict[i]:0})
            
        flag1= False
        flag2= False
        flag3= True
        
        # 第1个条件
        s_len = len(s)
        if s_len>=6 or s_len<=20:
            flag1=True
        
        # 第2个条件
        for i in range(s_len):
            char_map[s[i]] = char_map[s[i]]+1
        char_usage = list(char_map.values())
        c2_count = 0
        if sum(char_usage[0:10])<=0:
            c2_count = c2_count+1 
        if sum(char_usage[10:26])<=0:
            c2_count = c2_count+1
        if sum(char_usage[26:62])<=0:
            c2_count = c2_count+1
        if c2_count<=0:
            flag2=True
        
        # 第3个条件
        i=0
        while i<s_len-2:
            if s[i]==s[i+1]==s[i+2]:
                flag3 = False

        # 确定修改次数
        if flag1:
            if flag2:
                if flag3:
                    # strong
                    return 0
                else:
            else:
                if flag3:
                    # 2异常
                    # 使用replace
                    return c2_count
                else:
                    # 2,3异常

        else：
            if flag2:
                if flag3:
                    # 1异常
                    if s_len>20:
                        # 使用删除操作
                        return s_len-20
                    if s_len<6:
                        # 使用插入操作
                        return 6-s_len
                else:
                    # 1,3异常
            else:
                if flag3:
                    # 1,2异常
                    
                else:
                    # 1,2,3异常
        
        
        
           
                
            
                
            
            
            
            
            
