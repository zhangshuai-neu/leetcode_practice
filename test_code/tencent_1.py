while True:
    try:
        case_num = int(input())
        for j in range(case_num):
            num_map = {}
            #读取case并处理
            num_count = int(input())
            data = list(map(int,input().split()))
            for d in range(len(data)):
                if data[d] in num_map:
                    num_map[data[d]] = num_map[data[d]]+1
                else:
                    num_map.update({data[d]:1})

            print(num_map)
            num_list = num_map.values()
            print(num_list)
            num_list.sort()
            print(num_list)

            result = "NO"
            left_sum = 0
            right_sum = sum(num_list)
            for i in range(len(num_list)):
                left_sum = left_sum + num_list[i]
                right_sum = right_sum - num_list[i]
                if left_sum == right_sum:
                    result = "YES"
                    break
            print(result)
    except:
        break
