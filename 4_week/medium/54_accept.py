class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #遍历一次
        def visit_one_time(matrix, start_r, start_c, end_r, end_c):
            ret_list = []
            r = start_r
            c = start_c
            #只有一行
            if start_r == end_r:
                return matrix[start_r][start_c:end_c+1]
            #只有一列
            if start_c == end_c:
                while r <= end_r:
                    ret_list.append(matrix[r][start_c])
                    r = r+1
                return ret_list

            #上面一行
            while c <= end_c:
                ret_list.append(matrix[r][c])
                c = c+1
            c = c-1
            #右侧一列
            r = r+1
            while r <= end_r:
                ret_list.append(matrix[r][c])
                r = r+1
            r = r-1
            #下面一行
            c = c-1
            while c >= start_c:
                ret_list.append(matrix[r][c])
                c = c-1
            c = c+1
            #左侧一列
            r = r-1
            while r > start_r:
                ret_list.append(matrix[r][c])
                r = r-1
            return ret_list

        all_list = []
        if len(matrix) ==0:
            return all_list
        #按照圈数进行遍历
        row_len = len(matrix)
        col_len = len(matrix[0])
        itr_end = min(row_len//2+row_len%2, col_len//2+col_len%2)
        for i in range(itr_end):
            one_time_list = visit_one_time(matrix, i, i, row_len-1-i, col_len-1-i)
            all_list.extend(one_time_list)

        print(all_list)
        return all_list
# test code
# s = Solution()
# s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
