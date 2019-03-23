def atoi(s):
    # 比较特别的 Case "" "-000123"， "+asd", "+123123"
    if len(s) ==0:
        return 0
    # 1. 边界的问题，长度，大小
    # 1.1 符号
    unsined_s = s
    if s[0]=='-' or s[0]=='+': 
        unsined_s = s[1:]
    # 1.2 前导0
    i = 0
    unsined_sl = len(unsined_s)
    while i<unsined_sl:
        if unsined_s[i]!=0:
            break
    new_s = unsined_s[i:]
    
    # 1.2 边界检查 长度
    if s[0]=='-' and new_s>"2147483648" :
        return -2147483648
    if s[0]!='-' and new_s>"2147483647":
        return 2147483647
    
    # 1.3 出现非法字符
    for i in range(new_s):
        if ord(new_s[i])<ord('0') or ord(new_s[i])>ord('9'):
            return 0
    
    # 2. 从字符串的最低位置开始计算
    # 2.1 数字
    ret_num = 0
    reverse_new_s = "".join(list(new_s).reverse())
    reverse_new_sl = len(reverse_new_s)
    for i in range(reverse_new_sl):
        bitnum = ord(reverse_new_s[i]) - ord('0')
        ret_num = ret_num + bitnum*10**i
        
    # 2.1 符号
    if s[0]=='-':
        return -return_num
    else:
        return return_num
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
