# -*- coding:utf-8 -*-
while True:
    try:
        n, k = list(map(int,input().split()))
        count_list = list(map(int,input().split()))
        
        # 面包不足 或者 时间太短
        if sum(count_list) < k or k/n>8.0:
            print(-1)
            continue
        
        # 输出i, day天数, i当前获取位置，count获取数量
        day = 1
        i = 0
        count = 0
        while count<k:
            if count_list[i] > 8:
                count += 8
                count_list[i] -= 8
            else:
                # 从面连续一个或几个获取
                left_count = 8
                add_count = 0
                while i<day and left_count > 0:
                    if count_list[i] > left_count:
                        add_count += left_count
                        count_list[i] -= left_count
                        left_count = 0
                    else:
                        add_count += count_list[i]
                        left_count -= count_list[i]
                        i = i+1
                    # print("i", i, "day", day,"add_count:", add_count)
                count += add_count
            day = day + 1
        print(day-1)
    except:
        break
