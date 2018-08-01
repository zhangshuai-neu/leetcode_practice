class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_num = len(grid);
        column_num = len(grid[0]);
        result = 0;

        left2right=[];
        top2botom=[];

        for i in range(row_num):
            max_column = grid[i][0];
            for j in range(column_num):
                if(grid[i][j] > max_column):
                    max_column=grid[i][j];
            left2right.append(max_column);


        for j in range(column_num):
            max_row = grid[0][j];
            for i in range(row_num):
                if(grid[i][j] > max_row):
                    max_row=grid[i][j];
            top2botom.append(max_row);

        for i in range(row_num):
            for j in range(column_num):
                if top2botom[j] > left2right[i] : 
                    result = result + left2right[i] - grid[i][j];

                else:
                    result = result + top2botom[j] - grid[i][j];
        
        return result;
