import math

# 只处理一种长度
def process_1_length(l, k, all_result):
    if all_result[l][0] !=-1 and all_result[l][1] == k:
        return all_result[l][0]
    
    if k>l:
        return 1
    if k==l:
        return 2

    result_sum = 1 # 全部红
    K_num_range = math.ceil(l/k) 
    for i in range(l):
        for k_num in range(1, K_num_range):
            left_l = i-0-1
            right_l = l-i-k_num*k +1
            if right_l>0:
                result_sum = result_sum + process_1_length(left_l, k, all_result)
                result_sum = result_sum + process_1_length(right_l, k, all_result)
    return result_sum

# 处理所有范围
def process(a, b, k, all_result):
    result = 0
    for l in range(a,b+1):
        l_result = process_1_length(l, k, all_result)
        all_result[l][0] = l_result
        all_result[l][1] = k
        result = result + l_result
    return result

# [结果，k]
all_result = [[-1,0] for i in range(100000+1)]

while True:
    try:
        case_num, k = list(map(int,input().split()))
        for i in range(case_num):
            #读取case并处理
            a, b = list(map(int,input().split()))
            result = process(a, b, k, all_result)
            
            # 测试
            for i in range(a,b+1):
                print(all_result[i])
            print(result)
    except:
        break