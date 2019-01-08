class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s_len = len(S)
        ret_list = [ 0 for i in range(s_len)]
        left_list = [ 0 for i in range(s_len)]
        right_list = [ 0 for i in range(s_len)]
        
        i=0
        left = -10001
        while i<s_len:
            if S[i]==C:
                left = i
            left_list[i] = left
            i=i+1
        
        i=s_len-1
        right = -10001
        while i>-1:
            if S[i]==C:
                right = i
            right_list[i] = right
            i=i-1

        i=0
        while i<s_len:
            ret_list[i] = min(i-left_list[i], abs(i-right_list[i]))
            i=i+1
            
        return ret_list

#==============
s = Solution()
#s.shortestToChar("loveleetcode",'e')
s.shortestToChar("aaba","b")

        
        
