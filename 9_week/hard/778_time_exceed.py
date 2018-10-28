class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        
        #生成可达矩阵
        reach_matrix = []
        for i in range(N):
            temp_list = [ 0 for i in range(N)]
            reach_matrix.append(temp_list)
        reach_matrix[0][0]=1
        
        #未达dict
        unreach_dict = {}
        for i in range(1,N*N):
            unreach_dict.update({i:1})
        
        h0 = grid[0][0]
        
        #随着t增加，变化可达性
        t=0
        while reach_matrix[N-1][N-1]!=1:
            change_flag = True
            while change_flag:
                change_flag = False
                key_list = list(unreach_dict.keys())
                for l in key_list:
                    i=l//N
                    j=l%N
                    #周围有1
                    have_1_flag = False
                    if not have_1_flag and i-1>=0 and reach_matrix[i-1][j]==1:
                        have_1_flag=True
                    if not have_1_flag and i+1<N and reach_matrix[i+1][j]==1:
                        have_1_flag=True
                    if not have_1_flag and j-1>=0 and reach_matrix[i][j-1]==1:
                        have_1_flag=True
                    if not have_1_flag and j+1<N and reach_matrix[i][j+1]==1:
                        have_1_flag=True
                    
                    #可达
                    can_reach = False
                    h=grid[i][j]
                    if t>=h0 and t>=h:
                        can_reach=True
                    if have_1_flag and can_reach:               
                        reach_matrix[i][j]=1
                        unreach_dict.pop(l)
                        change_flag = True
            t=t+1

        return t-1
        
#=========================================
s=Solution()
'''
print(s.swimInWater([[0,2],[1,3]]))
#return 3

print(s.swimInWater([[3,2],[0,1]]))
#return 3
'''