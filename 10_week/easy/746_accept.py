class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost_len = len(cost)
        
        #记录到位置i时的最小cost
        min_list = [0,0]   
        
        for i in range(2,cost_len):
            c1 = cost[i-2] + min_list[i-2]
            c2 = cost[i-1] + min_list[i-1]
            min_list.append(min(c1,c2))
        
        c1 = min_list[cost_len-2]+ cost[cost_len-2]
        c2 = min_list[cost_len-1]+ cost[cost_len-1]
        
        return min(c1,c2)
