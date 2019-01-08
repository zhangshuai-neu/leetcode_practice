class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret_str = ""
        s_list = s.split(" ")
        for s1 in s_list:
            print(s1)
            l=list(s1)
            l.reverse()
            ret_str =ret_str + " " +"".join(l)
        return ret_str[1:]
