while True:
    try:
        N = int(input())
        s = input()
        rl = ""
        for i in range(N):
            ts = s[i*9:(i+1)*9]
            if ts[0]=='0':
                tsl = list(ts[1:])
                tsl.reverse()
                tsll = len(tsl)
                for j in range(8-tsll):
                    tsl.insert(0,' ')
                if len(rl)!=0:
                    rl = rl + " " +"".join(tsl)
                else:
                    rl = "".join(tsl)
                continue
            if ts[0]=='1':
                if len(rl)!=0:
                    rl = rl + " " + ts[1:]
                else:
                    rl = ts
        print(rl)
    except:
        break
