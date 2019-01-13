class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        square_list = []
        i=0
        for p in points:
            s = p[0]**2 + p[1]**2
            square_list.append([s,i])
            i = i+1
        
        def get_key(elem):
            return elem[0]
        
        square_list.sort(key = get_key)
        
        ret_list = []
        for i in range(K):
            ret_list.append( points[ square_list[i][1] ] )
        
        return ret_list
