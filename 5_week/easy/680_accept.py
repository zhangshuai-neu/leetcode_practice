class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_valid(s,error_count):
            result = True
            s_len = len(s)
            head = 0
            tail = s_len-1
            while head<tail:
                if s[head]!=s[tail]:
                    result = False      #出错
                    if error_count<1:   #是否能纠正
                        result = result or is_valid(s[head:tail],error_count+1)
                        result = result or is_valid(s[head+1:tail+1],error_count+1)
                    break
                head = head+1
                tail = tail-1

            return result

        ret_judge = is_valid(s,0)
        print(ret_judge)
        return ret_judge

#------------------------------------------
# 测试代码
#------------------------------------------
s = Solution()

#s.validPalindrome("aba")
# return True

#s.validPalindrome("abca")
# return True

s.validPalindrome("accbba")
# return False
