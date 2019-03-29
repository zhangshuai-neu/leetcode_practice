import copy
temp_list = [-1 for i in range(50)]
al = []
for i in range(40):
    al.append(copy.copy(temp_list))

def draw(m,n,count):
    count = count +1
    # 横线
    for i in range(50):
        if al[m][i]==0:
            al[m][i] = count
    # 竖线
    pre_count = count
    for i in range(40):
        if al[i][n]==0:
            if pre_count==count:
                count = count+1
            al[i][n] = count
    # 45度
    pre_count = count
    for i in range(50):
        if m-i<40 and m-i>=0 and n-i<50 and n-i>=0 and al[m-i][n-i]==0:
            if pre_count==count:
                count = count+1
            al[m-i][n-i] = count
        if m+i<40 and m+i>=0 and n+i<50 and n+i>=0 and al[m+i][n+i]==0:
            if pre_count==count:
                count = count+1
            al[m+i][n+i] = count
    # -45度
    pre_count = count
    for i in range(50):
        if m-i<40 and m-i>=0 and n+i<50 and n+i>=0 and al[m-i][n+i]==0:
            if pre_count==count:
                count = count+1
            al[m-i][n+i] = count
        if m+i<40 and m+i>=0 and n-i<50 and n-i>=0 and al[m+i][n-i]==0:
            if pre_count==count:
                count = count+1
            al[m+i][n-i] = count
        
    return count
    
while True:
    try:
        N = int(input())
        pl = []
        for i in range(N):
            pl.append(list(map(int,input().split())))
            m = pl[i][0]
            n = pl[i][1]
            al[m][n] = 0
        count = 0
        for i in range(N):
            m = pl[i][0]
            n = pl[i][1]
            count = draw(m,n,count)
        print(count)
    except:
        break
