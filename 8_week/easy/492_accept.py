class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt_area = int(area**0.5)
        
        while True:
            mod_num = area % sqrt_area
            if mod_num == 0:
                M = sqrt_area 
                L = area//M
                break
            sqrt_area = sqrt_area-1
            
        print(L,M)
        return [L,M]
            
