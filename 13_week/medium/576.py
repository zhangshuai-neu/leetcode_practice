class Solution:
    def findPaths(self, m, n, N, in_i, in_j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        # 空间换时间
        # result_list[time][i][j] 表示，在i,j这个位置，且能进行times移动时的结果
        # result_list[time][i][j] = result_list[time-1][i-1][j] +   
        #                           result_list[time-1][i+1][j] +
        #                           result_list[time-1][i][j-1] +
        #                           result_list[time-1][i][j+1] //(如果出界，替换为1。)
        #                            
        # 创建存放的数组[time][i][j]

        # 特殊情况
        if N==0:
            return 0
        import copy
        # 创建result_list
        l_n = [0 for j in range(n)]
        l_m = [copy.deepcopy(l_n) for i in range(m)]
        result_list = [copy.deepcopy(l_m) for t in range(N+1)]
        MOD = 1000000007
        for time in range(1,N+1):
            for i in range(m):
                for j in range(n):
                    count = 0
                    if i-1>=0:
                        count = count+result_list[time-1][i-1][j]
                    else:
                        count = count+1

                    if i+1<m:
                        count = count+result_list[time-1][i+1][j]
                    else:
                        count = count+1

                    if j-1>=0:
                        count = count+result_list[time-1][i][j-1]
                    else:
                        count = count+1

                    if j+1<n:
                        count = count+result_list[time-1][i][j+1]
                    else:
                        count = count+1
                    
                    result_list[time][i][j] = count % MOD

        return result_list[N][in_i][in_j]

"""
        # 方法2 递归 比较慢 超时
        # 递归函数
        def get_count(m, n, i ,j, time, result_list):
            MOD = 1000000007
            count = 0
            if time==1:
                #print("case1")
                count = result_list[1][i][j]
            else:
                if result_list[time][i][j]!=0 :
                    #print("case2")
                    # 之前计算过，空间换时间
                    count = result_list[time][i][j]
                else:
                    #print("case3")
                    #向上
                    if i-1>=0:
                        count = count + get_count(m, n, i-1 ,j, time-1, result_list)
                    else:
                        count = count + 1
                    #向下
                    if i+1<m:
                        count = count + get_count(m, n, i+1 ,j, time-1, result_list)
                    else:
                        count = count + 1
                    #向左
                    if j-1>=0:
                        count = count + get_count(m, n, i ,j-1, time-1, result_list)
                    else:
                        count = count + 1
                    #向右
                    if j+1<n:
                        count = count + get_count(m, n, i ,j+1, time-1, result_list)
                    else:
                        count = count + 1

            result_list[time][i][j]=count%MOD
            #print(i,j,time,count)
            return result_list[time][i][j]

        import copy
        # 特殊情况
        if N==0:
            return 0
        # 创建result_list
        l_n = [0 for j in range(n)]
        l_m = [copy.deepcopy(l_n) for i in range(m)]
        result_list = [copy.deepcopy(l_m) for t in range(N+2)]
        # 初始化
        if m==1 and n==1:
            result_list[1][0][0] = 4

        if n==1 and m>1:
            for i in range(1,m-1):
                result_list[1][i][0] = 2
            result_list[1][0][0] = result_list[1][m-1][0] = 3

        if m==1 and n>1:
            for j in range(1,n-1):
                result_list[1][0][j] = 2
            result_list[1][0][0] = result_list[1][0][n-1] = 3

        if m>1 and n >1:
            result_list[1][0][0]     =2
            result_list[1][0][n-1]   =2
            result_list[1][m-1][0]   =2
            result_list[1][m-1][n-1] =2
            for i in range(1,m-1):
                result_list[1][i][0] = result_list[1][i][n-1] =1
            for j in range(1,n-1):
                result_list[1][0][j] = result_list[1][m-1][j] =1
        return get_count(m, n, in_i ,in_j, N, result_list)
"""
#=====================
s = Solution()
#print(s.findPaths(2,2,2,0,0)) #return 6
#print(s.findPaths(1,3,3,0,1)) #return 12
#print(s.findPaths(2,3,8,1,0)) #return 1104
#print(s.findPaths(3,2,5,1,1))  #return 109
#print(s.findPaths(3,2,5,1,1))  #return 109
print(s.findPaths(30,24,23,26,12))


