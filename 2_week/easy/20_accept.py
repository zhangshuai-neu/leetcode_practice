class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        str_len = len(s)
        for i in range(str_len):
            #左侧
            if s[i] == '(' or  s[i] == '[' or s[i] == '{':
                stack.append(s[i])
                continue
            
            #右侧
            if s[i] == ')' or  s[i] == ']' or s[i] == '}':
                if len(stack) == 0:
                    return False
                if s[i] == ')' and stack[len(stack)-1] == '(':
                    stack.pop()
                    continue
                if s[i] == ']' and stack[len(stack)-1] == '[':
                    stack.pop()
                    continue
                if s[i] == '}' and stack[len(stack)-1] == '{':
                    stack.pop()
                    continue
                return False
            
        #最后stack为空
        if len(stack) != 0:
            return False
        
        return True
