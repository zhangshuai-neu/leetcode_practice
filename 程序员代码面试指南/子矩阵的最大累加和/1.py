# 输入
# m行 n列 
# 矩阵
while True:
    try:
        # 输入
        m,n= list(map(int,input().split()))
        data = []
        for i in range(m):
            data.append( list(map(int,input().split())) )
        # 处理
        dp = []
        max_dp = 
        # j是列,合并列，按照最大子数组来计算
        for j in range(m):
            for i in range(m):
                d = sum(data[:][j])
            
    except:
        break
