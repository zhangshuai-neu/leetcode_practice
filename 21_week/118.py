class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret_list = []
        for i in range(1,numRows+1):
            new_list = [1 for j in range(i)]
            ret_list.append(new_list)

        for i in range(2,numRows):
            for j in range(1,i):
                ret_list[i][j] = ret_list[i-1][j-1] + ret_list[i-1][j]
        
        return ret_list
        
#================
# 测试
#================
s = Solution()
s.generate(5)
