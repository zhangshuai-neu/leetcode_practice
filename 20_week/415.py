class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        n1_l = list(num1)
        n1_l.reverse()  #从低位开始处理
        
        n2_l = list(num2)
        n2_l.reverse()
        
        n1_l_len = len(n1_l)
        n2_l_len = len(n2_l)
        min_len = min(n1_l_len, n2_l_len)
        
        # int(num1) + int(num2) => ret_l
        ret_l = []
        carry = 0 #进位
        for i in range(min_len):
            n = ord(n1_l[i])+ord(n2_l[i]) - 2*ord('0') + carry
            if n>9:
                carry = 1
                n = n%10
            else:
                carry = 0
            ret_l.append(n)
        
        if min_len == n1_l_len:
            i=min_len
            while i<n2_l_len:
                n = ord(n2_l[i]) - ord('0') + carry
                if n>9:
                    carry = 1
                    n = n%10
                else:
                    carry = 0
                ret_l.append(n)
                i=i+1
            if carry==1:
                ret_l.append(1)
        else:
            i=min_len
            while i<n1_l_len:
                n = ord(n1_l[i]) - ord('0') + carry
                if n>9:
                    carry = 1
                    n = n%10
                else:
                    carry = 0
                ret_l.append(n)
                i=i+1
            if carry==1:
                ret_l.append(1)
        
        # ret_l => ret_str
        ret_l.reverse() # 再次逆序，从高位开始处理
        ret_str = ""
        for val in ret_l:
            ret_str = ret_str + chr( val + ord('0') )
        return ret_str
