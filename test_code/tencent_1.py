

while True:
    try:
        case_num = int(input())
        num_map = {}
        for j in range(case_num):
            #读取case并处理
            num_count = int(input())
            data = list(map(int,input().split()))
            for d in range(data):
                if d in num_map:
                    num_map[d] = num_map[d]+1
                else:
                    num_map.update({d:1})
            
            num_list = num_map.values()
            num_list.sort(reverse=False)

            result = "NO"
            left_sum = 0
            right_sum = sum(num_list)
            for i in range(len(num_list)):
                left_sum = left_sum + num_list[i]
                right_sum = right_sum - num_list[i]
                if left_sum == right_sum:
                    result = "YES"
            print(result)
    except:
        break