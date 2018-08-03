class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        test_mask = 1
        for i in range(31):
            if x&test_mask != y&test_mask:
                count = count + 1
            test_mask = test_mask << 1
        
        return count
