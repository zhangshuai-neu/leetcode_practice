# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        # 用list表示栈，stack[0]为栈顶
        stack = []
        ret_ni = None
        
        i=0
        j=0
        s_len = len(s)
        
        while i<s_len:
            if s[i] == '-' or (s[i]<='9' and s[i]>='0'):
                # 数字
                j=i+1
                while j<s_len and s[j]<='9' and s[j]>='0':
                    j=j+1
                    
                num = int(s[i:j])
                if len(stack) != 0:
                    stack[0].add( NestedInteger(num) )
                else:
                    stack.insert(0, NestedInteger(num) )
                i=j
                continue
            
            if s[i] == '[':
                # NestedInteger
                new_ni = NestedInteger()
                stack.insert(0,new_ni)
                i=i+1
                continue
                
            if s[i] == ',':
                # 分隔符
                i=i+1
                continue
                
            if s[i] == ']':
                # 结束符
                if len(stack)!=0:
                    internal_ni = stack.pop(0)
                    if len(stack)!=0:
                        stack[0].add(internal_ni)
                    else:
                        ret_ni = internal_ni
                i=i+1
                
            return ret_ni

