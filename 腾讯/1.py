while True:
    try:
        s = input().split()
        m, n = list(map(int,s))
        coin_list = []
        
        for i in range(n):
            coin = int(input())
            coin_list.append(coin)
        coin_list.sort()
        if coin_list[0]!=1:
            print(-1)
        
        # 

    except:
        break