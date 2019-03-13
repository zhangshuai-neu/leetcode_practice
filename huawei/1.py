while True:
    try:
        # 读取N和M
        nm_str = input()
        nm_str_list = nm_str.split()
        N = int(nm_str_list[0])
        M = int(nm_str_list[1])
        
        # 学生成绩
        score_str_list = input()
        score_str_list = score_str_list.split()
        score_int_list = []
        for i in range(N):
            score_int_list.append(int(score_str_list[i]))
        
        print_list = []
        for i in range(M):
            cab_str_list = input()
            cab_str_list = cab_str_list.split()
            c = cab_str_list[0]
            a = int(cab_str_list[1])
            b = int(cab_str_list[2])
            if c=="Q":
                if a<=b:
                    print_list.append(max(score_int_list[a-1:b]))
                else:
                    print_list.append(max(score_int_list[b-1:a]))
            if c=="U":
                score_int_list[a-1] = b
        for val in print_list:
            print(val)
    except:
        break
