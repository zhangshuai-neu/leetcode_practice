class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        # 空间换时间
        # result_list[i][j][time] 表示，在i,j这个位置，且能进行times移动时的结果
        # result_list[i][j][time] =  递推式 有点问题
        # 创建存放的数组[i][j][time]

        # 迭代函数
        def get_count(m, n, i ,j, time, result_list):
            count = 0
            if time==1:
                count = result_list[i][j][1]
            else:
                if time>1 and result_list[i][j][time]!=0 :
                    # 之前计算过，空间换时间
                    count = result_list[i][j][time]
                else:

            result_list[i][j][time]=count
            print(i ,j, time, count)
            return count

        # 特殊情况
        if N==0:
            return 0

        l_N = [0 for t in range(N+2)]
        l_n = [l_N.copy() for j in range(n)]
        result_list = [l_n.copy() for i in range(m)]

        # 初始化
        if m==1 and n==1:
            result_list[0][0][1] = 4

        if n==1 and m>1:
            result_list[0][0][1] = result_list[m-1][0][1] = 3
            for i in range(1,m-1):
                result_list[i][0][1] = 2
        if m==1 and n>1:
            result_list[0][0][1] = result_list[0][n-1][1] = 3
            for j in range(1,n-1):
                result_list[0][j][1] = 2

        if m>1 and n >1:
            result_list[0][0][1]     =2
            result_list[0][n-1][1]   =2
            result_list[m-1][0][1]   =2
            result_list[m-1][n-1][1] =2
            for i in range(1,m-1):
                result_list[i][0][1] = result_list[i][n-1][1] =1
            for j in range(1,n-1):
                result_list[0][j][1] = result_list[m-1][j][1] =1
        
        return get_count(m, n, i ,j, N, result_list)

#=====================
s = Solution()
#print(s.findPaths(2,2,2,0,0)) #return 6
print(s.findPaths(1,3,3,0,1)) #return 12
