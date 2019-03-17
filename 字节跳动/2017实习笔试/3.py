def getall(sl):
    sl_len = len(sl)
    if sl_len <2:
        return sl
    all_list = []
    for i in range(sl_len):
        s = sl[i]
        sl.pop(i)
        #构建排列
        t_all_list= getall(sl)
        for t in t_all_list:
            all_list.append(s+t)
        sl.insert(i,s)
    return all_list
    
def isk(s,k):
    sl= list(s)
    sl_len = len(sl)
    count =0 
    for i in range(sl_len):
        c = sl.pop(0)
        sl.append(c)
        if "".join(sl) == s:
            count = count+1
    return count==k

while True:
    try:
        n,k=list(map(int, input().split()))
        sl = []
        for i in range(n):
            sl.append(input())
        # 获取所有的全排列列表
        sl_all = getall(sl)
        # 判断是否为k权重
        count = 0
        for s in sl_all:
            if isk(s,k):
                count = count+1
        print(count)
    except:
        break
