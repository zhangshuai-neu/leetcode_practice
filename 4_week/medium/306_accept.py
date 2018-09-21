class Solution:
    def isAdditiveNumber(self, num):
        """    
        :type num: str
        :rtype: bool
        """
        def isAdditive(num_str):
            result = False
            num_str_len = len(num_str)
            #遍历num1
            num1_len = 1
            while num1_len<num_str_len/2:
                if num1_len>1 and num_str[0]=='0':
                    #没必要继续，首字母不能为0
                    break;
                #获取num1的值
                num1 = int(num_str[0:num1_len])

                #遍历num2
                num2_len = 1
                while num2_len<num_str_len/2:
                    if num2_len>1 and num_str[num1_len]=='0':
                        #没必要继续，首字母不能为0
                        break;
                    num2 = int(num_str[num1_len:num1_len+num2_len])

                    #判断num1于num2的组合
                    sum_str = str(num1+num2)
                    sum_len = len(sum_str)
                    lss_i = num1_len+num2_len    #left_str_start_index
                    left_str_len = num_str_len-lss_i
                    if left_str_len >= sum_len:
                    	# debug_zs
                        print("num1:",num1,"num2:",num2,"sum:",sum_str,"left:",num_str[lss_i:lss_i+sum_len])
                        if sum_str == num_str[lss_i:lss_i+sum_len]:
                            # num1 和 num2 可以，进行后续判断
                            result = True
                            if sum_len<left_str_len:
                                result = result and isAdditive(num_str[num1_len:num_str_len])
                            
                            if result:
                                return result
                    else:
                        #没必要继续，num1和num2太大
                        break;
                    #迭代 while
                    num2_len = num2_len+1
                #迭代 while
                num1_len = num1_len+1
            return result
        
        print(num)
        result = isAdditive(num)
        print(result)
        return result

        
#------------------------------------------
# 测试代码
#------------------------------------------
s = Solution()

s.isAdditiveNumber("112")
#return True

s.isAdditiveNumber("112358")
#return True

s.isAdditiveNumber("199100199")
#return True
