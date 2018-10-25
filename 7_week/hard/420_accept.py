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

        def takeThird(elem):
            return elem[2]
        
        flag1= False
        flag2= False
        flag3= True
        
        # 第1个条件
        s_len = len(s)
        
        if s_len>=6 and s_len<=20:
            flag1=True
        
        # 第2个条件
        digit_sign=1
        lower_sign=1
        upper_sign=1
        for i in range(s_len):
            if ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                digit_sign=0
            if ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
                lower_sign=0
            if ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
                upper_sign=0
        c2_count = digit_sign+lower_sign+upper_sign
        if c2_count<=0:
            flag2=True
        
        # 第3个条件,同时记录aaaa：重复位置和重复次数
        repeat_list = []
        repeat_can_delete_count = 0
        max_replace_count = 0
        if s_len>=3:
            i=0
            while i<s_len:
                start=i
                repeat_count=0
                while start+repeat_count<s_len and s[i]==s[start+repeat_count]:
                    repeat_count=repeat_count+1
                if repeat_count>=3:
                    repeat_list.append([start,repeat_count,repeat_count%3])
                    repeat_can_delete_count = repeat_can_delete_count+repeat_count-2
                max_replace_count = max_replace_count+repeat_count//3

                i=i+repeat_count
        repeat_list_len = len(repeat_list)
        if max_replace_count>0:
            flag3=False

        print(flag1,flag2,flag3)
        
        # 确定修改次数
        if flag1:
            if flag2:
                if flag3:
                    # strong
                    return 0
                else:
                    # 3异常,只能进行replace
                    return max_replace_count
            else:
                if flag3:
                    # 2异常
                    # 使用replace
                    return c2_count
                else:
                    # 2,3异常
                    # 2,3异常都用replace解决，看哪一种更多
                    # 异常3的replace次数与repeat_list相关
                    return max(max_replace_count, c2_count)
        else:
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
                    #短 使用插入操作
                    if s_len<6:
                        #只有一下集中可能
                        # aaaB1 / B1aaa / Baaa1
                        # 只要插入一个新字符即可，比如aaAaB1
                        return 1
                        
                    #长 使用 delete 和 replace 操作
                    if s_len>20:
                        op_count=0
                        # 先用delete缓解1，3
                        # 如果不能delete到<=20，
                        over_len = s_len-20
                        if repeat_can_delete_count>=over_len:
                            # 如果能delete到<=20, 那就将所有重复都变成3m+2的形式，这样replace最有效率
                            # 转化为问题3
                            del_count = 0
                            while(del_count<over_len):
                                # 一遍遍的重复,将重复串变成3m+2的形式
                                repeat_list.sort(key=takeThird)
                                for k in range(repeat_list_len):
                                    rs=repeat_list[k][0]
                                    rl=repeat_list[k][1]
                                    if rl<3:
                                        continue
                                    if rl%3==0:
                                        #减1
                                        minus_num=1
                                    else:
                                        if rl%3==1:
                                            #减2
                                            minus_num=2
                                        else:
                                            if rl%3==2:
                                                #减3
                                                minus_num=3
                                    if del_count+minus_num>over_len:
                                        #不要过度减
                                        minus_num = over_len-del_count
                                        
                                    s=s[0:rs]+s[rs+minus_num:]
                                    del_count=del_count+minus_num
                                    repeat_list[k][1]=repeat_list[k][1]-minus_num
                                    repeat_list[k][2]=repeat_list[k][1]%3
                                    #删除导致的位置移动
                                    for bi in range(repeat_list_len):
                                        if repeat_list[bi][0]>rs:
                                            repeat_list[bi][0]=repeat_list[bi][0]-minus_num
                                    if del_count>=over_len:
                                        break
                        else:
                            # 如果不能delete到<=20, 说明如果一直删除重复，会消除异常3
                            # 转化成异常1
                            del_count = 0
                            pre_del_count = -1
                            while(pre_del_count<del_count): #无法再删除了
                                # 一遍遍的重复,将重复串变成3m+2的形式
                                pre_del_count=del_count
                                repeat_list.sort(key=takeThird)
                                for k in range(repeat_list_len):
                                    rs=repeat_list[k][0]
                                    rl=repeat_list[k][1]
                                    if rl<3:
                                        continue
                                    if rl%3==0:
                                        #减1
                                        minus_num=1
                                    else:
                                        if rl%3==1:
                                            #减2
                                            minus_num=2
                                        else:
                                            if rl%3==2:
                                                #减3
                                                minus_num=3
                                    s=s[0:rs]+s[rs+minus_num:]
                                    del_count=del_count+minus_num
                                    repeat_list[k][1]=repeat_list[k][1]-minus_num
                                    repeat_list[k][2]=repeat_list[k][1]%3
                                    #删除导致的位置移动
                                    for bi in range(repeat_list_len):
                                        if repeat_list[bi][0]>rs:
                                            repeat_list[bi][0]=repeat_list[bi][0]-minus_num
                        op_count = del_count+self.strongPasswordChecker(s)
                        return op_count

            else:
                if flag3:
                    # 1,2异常
                    # 字符串短，使用add
                    if s_len<6:
                        return max(6-s_len,c2_count)
                    # 字符串长，使用delete和replace
                    if s_len>20:
                        return s_len-20 + c2_count
                else:
                    # 1,2,3异常
                    #短 使用插入操作
                    if s_len<6:
                        # 有以下可能
                        if c2_count==1:
                            #有2种字符 aaaB aaaaB aaaBa
                            #使用insert就可解决
                            return 6-s_len
                        if c2_count==2:
                            #只有1种字符 aaa aaaa aaaaa
                            if s_len==5:
                                return 2
                            else:
                                return 6-s_lens
                        if c2_count==3:
                            # 特别情况 "..."  "...."  "....."
                            # "..."  "...#"  "...##"
                            # 缺少3种字符
                            return 3
                    
                    #长 使用delete和replace操作
                    if s_len>20:
                        op_count=0
                        # 先用delete缓解1，3
                        # 如果不能delete到<=20，
                        over_len = s_len-20
                        if repeat_can_delete_count>=over_len:
                            # 如果能delete到<=20, 那就将所有重复都变成3m+2的形式，这样replace最有效率
                            # 转化为问题2，3
                            del_count = 0
                            while(del_count<over_len):
                                # 一遍遍的重复,将重复串变成3m+2的形式
                                repeat_list.sort(key=takeThird)
                                for k in range(repeat_list_len):
                                    rs=repeat_list[k][0]
                                    rl=repeat_list[k][1]
                                    if rl<3:
                                        continue
                                    if rl%3==0:
                                        #减1
                                        minus_num=1
                                    else:
                                        if rl%3==1:
                                            #减2
                                            minus_num=2
                                        else:
                                            if rl%3==2:
                                                #减3
                                                minus_num=3
                                    if del_count+minus_num>over_len:
                                        #不要过度减
                                        minus_num = over_len-del_count
                                    s=s[0:rs]+s[rs+minus_num:]
                                    del_count=del_count+minus_num
                                    repeat_list[k][1]=repeat_list[k][1]-minus_num
                                    repeat_list[k][2]=repeat_list[k][1]%3
                                    #删除导致的位置移动
                                    for bi in range(repeat_list_len):
                                        if repeat_list[bi][0]>rs:
                                            repeat_list[bi][0]=repeat_list[bi][0]-minus_num
                                    if del_count>=over_len:
                                        break
                        else:
                            # 如果不能delete到<=20, 说明如果一直删除重复，会消除异常3
                            # 转化成异常1，2
                            del_count = 0
                            pre_del_count = -1
                            while(pre_del_count<del_count): #无法再删除了
                                # 一遍遍的重复,将重复串变成3m+2的形式
                                repeat_list.sort(key=takeThird)
                                pre_del_count=del_count
                                for k in range(repeat_list_len):
                                    rs=repeat_list[k][0]
                                    rl=repeat_list[k][1]
                                    if rl<3:
                                        continue
                                    if rl%3==0:
                                        #减1
                                        minus_num=1
                                    else:
                                        if rl%3==1:
                                            #减2
                                            minus_num=2
                                        else:
                                            if rl%3==2:
                                                #减3
                                                minus_num=3
                                    if del_count+minus_num>over_len:
                                        #不要过度减
                                        minus_num = over_len-del_count
                                    s=s[0:rs]+s[rs+minus_num:]
                                    del_count=del_count+minus_num
                                    repeat_list[k][1]=repeat_list[k][1]-minus_num
                                    repeat_list[k][2]=repeat_list[k][1]%3
                                    #删除导致的位置移动
                                    for bi in range(repeat_list_len):
                                        if repeat_list[bi][0]>rs:
                                            repeat_list[bi][0]=repeat_list[bi][0]-minus_num
                                    
                        op_count = del_count+self.strongPasswordChecker(s)
                        return op_count

#===================================================================================
s=Solution()

'''
print(s.strongPasswordChecker("aaa111"))
#return 2


print(s.strongPasswordChecker("1111111111"))
#return 3


print(s.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa"))
#return 7


print(s.strongPasswordChecker("ababababababababaaaaa"))
#return 3


print(s.strongPasswordChecker("aaaabbaaabbaaa123456A"))
#return 3


print(s.strongPasswordChecker("aaaabaaaaaa123456789F"))
#return 3

print(s.strongPasswordChecker("aaaaaaaAAAAAA6666bbbbaaaaaaABBC"))
#return 13
'''

print(s.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa"))
#return 



