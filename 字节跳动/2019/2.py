while True:
    try:
        N = int(input())
        s_list = []
        for i in range(N):
            s_list.append(input())
            
        for s in s_list:
            sl = list(s)
            s_len = len(sl)
            i=0
            while i<s_len:
                # aaa
                if i+2<s_len:
                    if sl[i]==sl[i+1] and sl[i+1]==sl[i+2]:
                        sl.pop(i+2)
                        s_len = s_len-1
                        continue
                # aabb
                if i+3<s_len:
                    if sl[i]==sl[i+1] and sl[i+2]==sl[i+3]:
                        sl.pop(i+3)
                        s_len = s_len-1
                        continue
                # 正常
                i=i+1
            print("".join(sl))
    except:
        break
