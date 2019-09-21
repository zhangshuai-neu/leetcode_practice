# 只能进行 +1 /2 /3 的操作，判断最少多少次变为1

def process(m, count, res_list):
    m = int(m)
    # print("debug:", m, count, res_list)
    
    if m == 0:
        return 1
    if m == 1:
        return 0
        
    if count >= res_list[0]:
        return res_list[0]
        
    if m%2 == 0:
        count2 = count + 1
        res2 = process(m/2, count2, res_list)
        if res2 + count2 < res_list[0]:
            res_list.insert(0, res2 + count2)
            res_list.pop()
        # print("debug2:", res2, count2, res_list)
    if m%3 == 0:
        count3 = count + 1
        res3 = process(m/3, count3, res_list)
        if res3 + count3 < res_list[0]:
            res_list.insert(res3, res3 + count3)
            res_list.pop()
        # print("debug3:", res3, count3, res_list)
    
    count1 = count +1
    res1 = process(m+1, count1, res_list)
    if res1 + count1 < res_list[0]:
        res_list.insert(0, res1 + count1)
        res_list.pop()
    # print("debug1:", res1, count1, res_list)

    return res_list[0]
    
while(True):
    try:
        m = int(input())
        res_list = [100]
        res = process(m, 0, res_list) # 100 操作上限
        print(res_list[0])
    except:
        break