class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.list[len(self.list)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list)
        
#-------------------------------------
# 测试代码
#-------------------------------------
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
