class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        方法说明：
        计算该点到最近0的距离，只允许上下左右移动
        从0处开始的传播
        0到某一点的step，为周围点到该点的加一步距离
        多次迭代。迭代次数为最大step数
        """
        # m行，n列
        M=len(matrix)
        N=len(matrix[0])
        
        #判断矩阵是否发生变化
        mod_flag=False
        
        while True:
            mod_flag=False
            for i in range(M):
                for j in range(N):
                    #为0，跳过
                    if matrix[i][j]==0:
                        continue
                    
                    #不为0，计算
                    left=right=up=down=10001    #极大，因为元素数不超过10000
                    #左侧
                    if j>0:
                        left = matrix[i][j-1]
                    #右侧
                    if j<N-1:
                        right = matrix[i][j+1]
                    #上侧
                    if i>0:
                        up = matrix[i-1][j]
                    #下侧
                    if i<M-1:
                        down = matrix[i+1][j]
                    
                    #传播后的值
                    val = min(left,right,up,down)+1
                        
                    if  val != matrix[i][j]:
                        matrix[i][j]=val
                        mod_flag = True

            if mod_flag==False:
                #停止迭代，所有传播停止
                break
        print(matrix)
        return matrix

#======================================
# 测试代码
#======================================
s = Solution()

s.updateMatrix([[0],[1]])

s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
#return [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
#return [[0, 0, 0], [0, 1, 0], [1, 2, 1]]



