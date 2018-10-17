class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        str_map = {}
        repeat_flag = False
        different_count = 0
        different_list = []
        A_len = len(A)
        B_len = len(B)
        #长度是否一致
        if A_len != B_len:
            #no
            return False
        else:
            #yes
            for i in range(A_len):
                if not repeat_flag:
                    if A[i] not in str_map:
                        str_map.update({A[i]:1})
                    else:
                        str_map.update({A[i]:1+str_map[A[i]]})
                        if str_map[A[i]]>1:
                            repeat_flag = True
                    
                if A[i]!=B[i]:
                    different_count = different_count+1
                    different_list.append(i)
            
            #是否能转换
            if different_count!=2:
                if different_count==0 and repeat_flag:
                    return True
                return False
            else:
                pi=different_list[0]
                ni=different_list[1]
                if A[pi]==B[ni] and B[pi]==A[ni]:
                    return True
                else:
                    return False
            
