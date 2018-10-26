class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #深度遍历 判断能否到达 grid[N-1][N-1]
        def deep_search(grid,t,si,sj,pre_map):
            N=len(grid)

            
            return result

        # t一定在 0 和 max(grid)之间
        N = len(grid)
        max_t = 0
        for i in range(N):
            max_t=max( max_t, max(grid[i]) )

        pre_map={}


        big_t=max_t
        small_t=0
        mid_t=(big_t+small_t)//2
        while small_t<big_t:
            if deep_search(grid,mid_t,0,0,pre_map):
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