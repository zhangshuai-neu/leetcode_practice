class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #字符串反转
        def reverse_str(str):
            str_l = list(str)
            str_l.reverse()
            return "".join(str_l)

        #去掉一个括号ch，返回所有可能
        def rm_pare(str,ch):        
            possible_str = []
            str_len = len(str)
            for i in range(str_len):
                if str[i]==ch:
                    if i>0 and str[i-1]==ch:
                        continue
                    possible_str.append(str[0:i]+str[i+1:str_len])
            return possible_str
        
        #处理符号ch,使字符串合理
        #ch为"("或者")"
        #输入的字符串不合法
        def make_str_valid(s,ch):
            #处理第一个非法ch
            valid_str_list=[]
            valid_sub_str_list = []
            stack_count = 0
            str_len = len(s)
            for i in range(str_len):
                if s[i]=='(' or s[i]==')':#以括号终止
                    #括号处理
                    if s[i]==ch:
                        stack_count = stack_count-1
                    else:
                        stack_count = stack_count+1

                    if stack_count<0:   #出现不合理的情况,比如")"过多
                        valid_sub_str_list = rm_pare(s[0:i+1],ch)
                        if i+1>=str_len:
                            for a in range(len(valid_sub_str_list)):
                                if valid_sub_str_list[a] not in valid_str_list:
                                    valid_str_list.append(valid_sub_str_list[a])
                        else:
                            for j in range(len(valid_sub_str_list)):
                                two_sub_str_list = make_str_valid(valid_sub_str_list[j]+s[i+1:],ch)
                                for a in range(len(two_sub_str_list)):
                                    if two_sub_str_list[a] not in valid_str_list:
                                        valid_str_list.append(two_sub_str_list[a])
                        break
                    else:
                        if i+1>=str_len:
                            valid_str_list.append(s)
                else:
                    if i+1>=str_len and stack_count>=0:
                        valid_str_list.append(s)
            return valid_str_list
                            
        str_list = make_str_valid(s,")")

        valid_str_list = []
        str_list_len = len(str_list)

        for i in range(str_list_len):
            #合法化
            temp_str_list=make_str_valid(reverse_str(str_list[i]),"(")
            #再次逆序
            for j in range(len(temp_str_list)):
                valid_str_list.append(reverse_str(temp_str_list[j]))
                
        if len(valid_str_list)==0:
            valid_str_list=[""]
       
        print(valid_str_list)
        return valid_str_list
        
#------------------------------------------
# 测试代码
#------------------------------------------
s = Solution()

s.removeInvalidParentheses("()())r)")

#s.removeInvalidParentheses("()())a)b)")

s.removeInvalidParentheses("()())()")
# return ["()()()", "(())()"]

s.removeInvalidParentheses("()())()())")
# return ['(())(())', '(())()()', '()()(())', '()()()()']

s.removeInvalidParentheses("(a)())()")
# return ["(a)()()", "(a())()"]

s.removeInvalidParentheses(")(")
# return [""]

s.removeInvalidParentheses("")
# return [""]

s.removeInvalidParentheses("(r(()()(")
# return ["r()()","r(())","(r)()","(r())"]

