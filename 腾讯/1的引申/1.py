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

        dp = [ m for i in range(m+1) ]      #记录最简单组合的数量
        dp_set = [[] for i in range(m+1) ]  #记录每个值的最简单组合
        dp[0] = 0
        dp[1] = 1
        s_coin = set([1])
        for i in range(2,m+1):
            for j in range(n):
                if coin_list[j]==i:
                    dp[i] = 1
                    dp_set[i] = []
                    dp_set[i].append(coin_list[j])
                    continue
                if coin_list[j]>i:
                    break
                if coin_list[j]<i:
                    if dp[i]> dp[i-coin_list[j]]+1:
                        dp[i] = dp[i-coin_list[j]]+1
                        dp_set[i] = []
                        dp_set[i].extend(dp_set[i-coin_list[j]])
                        dp_set[i].append(coin_list[j])
        max_set = len(dp_set[1])
        for i in range(2,m+1):
            print(dp_set[i])
            max_set = max(max_set,len(dp_set[i]))
        print(max_set)
    except:
        break