class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        if num<0:
            #负数转为补码形式
            num = (1<<32) + num
        
        left_num = num
        ret_str_list = []
        while left_num !=0:
            mod = left_num % 16
            ret_str_list.insert(0,hex(mod)[2:])
            left_num = left_num // 16

        ret_str = "".join(ret_str_list)
        return ret_str
        
        
s = Solution()
s.toHex(26)
s.toHex(-1)
