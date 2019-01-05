class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def test(num):
            n = num
            while num>0:
                d = num%10
                if d==0 or n%d!=0:
                    return False
                num = num//10
            return True
            
        ret_list = []
        val = left
        while val<=right:
            if test(val):
                ret_list.append(val)
            val = val+1
        return ret_list
