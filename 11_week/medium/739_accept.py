class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 1) 最坏的做法是 n!，每次都遍历后面的元素
        # 
        # 2) 快速方法
        #   倒着解决，用hash记录i之后的T出现情况（每种温度的最小索引）
        #   复杂度为 最坏为70*n

        T_len = len(T)
        t_dict = {T[T_len-1]:T_len-1}   #hash表
        big_list = [0]                  #存放结果

        i=T_len-2
        while i>=0:
            t=T[i]

            #比t大的温度的最小索引
            min_i = 30001
            l = list(t_dict.keys())
            for big_t in l:
                if big_t>t:
                    min_i = min(t_dict[big_t],min_i)
            if min_i == 30001:
                #没有warmer
                big_list.insert(0,0)
            else:
                #距离warmer的长度
                big_list.insert(0,min_i-i)

            # 更新dict，记录t出现的最早位置
            t_dict.update({t:i})

            i=i-1

        return big_list

