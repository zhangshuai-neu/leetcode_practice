def getkey(elem):
    return elem[0]
while True:
    try:
        n = int(input())
        sl = []
        for i in range(n):
            sl.append(input())
        sym_list = ['A','B','C','D','E','F','G','H','I','J']
        sym_num_dict = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
        sym_num_list = []
        for c in sym_list:
            count = 0
            flag = 1 # 前导0，判断
            for s in sl:
                s_len = len(s)
                i=s_len-1
                while i>=0:
                    if s[i]==c:
                        count = count + sym_num_dict[c] + 10**(s_len-1-i)
                    i=i-1
                if s_len>0 and s[0]==c:
                    flag=0 # c可能为前导0
            sym_num_dict.update({c:count})
            sym_num_list.append([count,c,flag,1]) # 影响,符号，前导0，数字
        sym_num_list.sort(reverse=True)
        # 处理前导0
        i = 9
        while i >=0:
            # flag为1
            if sym_num_list[i][2]==1:
                sym_num_list[i][3]=0
                break
            i=i-1
        # 处理结果
        ret_val = 0
        num = 9
        for i in range(10):
            # 不是前导0
            if sym_num_list[i][3]==1:
                ret_val = ret_val + num * sym_num_list[i][0]
                num = num -1
        print(ret_val)
    except:
        break
