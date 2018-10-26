class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #深度遍历 判断能否到达 grid[N-1][N-1]
        def deep_search(grid,t,i,j,reach_matrix):
            N=len(grid)
            if reach_matrix[N-1][N-1]==1:
                return True
            result = False
            next = [[1,0],[-1,0],[0,1],[0,-1]]
            for step in range(4):
                next_i = i+next[step][0] 
                next_j = j+next[step][1] 
                if 0<=next_i and next_i<N and 0<=next_j and next_j<N:
                    h=grid[0][0]
                    next_h=grid[next_i][next_j]
                    if reach_matrix[next_i][next_j]==0 and t>=h and t>=next_h:
                        #reach_matrix[next_i][next_j]==0 避免重复
                        reach_matrix[next_i][next_j]=1
                        result = result or deep_search(grid,t,next_i,next_j,reach_matrix)
                if result:
                    break
            return result

        #生成可达矩阵，N^N
        def init_reach_matrix(N):
            reach_matrix=[]
            for i in range(N):
                temp_list = [0 for j in range(N)]
                reach_matrix.append(temp_list)
            reach_matrix[0][0]=1
            return reach_matrix

        # t一定在 0 和 N*N-1之间(题目给出)
        N = len(grid)
        max_t = N*N-1
        big_t=max_t
        small_t=0
        mid_t=(big_t+small_t)//2
        while small_t<big_t:
            reach_matrix = init_reach_matrix(N);

            if deep_search(grid,mid_t,0,0,reach_matrix):
                big_t=mid_t
            else:
                small_t=mid_t+1
            mid_t=(big_t+small_t)//2
        
        return mid_t
        
#=========================================
s=Solution()
'''
print(s.swimInWater([[0,2],[1,3]]))
#return 3

print(s.swimInWater([[3,2],[0,1]]))
#return 3
'''
l=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(s.swimInWater(l))