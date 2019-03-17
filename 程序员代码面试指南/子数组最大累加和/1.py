# 输入
# 数组

while True:
    try:
        l = list(map(int,input().split()))
        ll = len(l)
        # dp[i] 表示[0-i]的子数组最大和
        dp = [0 for i in range(ll)] 
        dp[0] = l[0]
        for i in range(1,ll):
            if dp[i-1]>0:
                dp[i] = dp[i-1]+l[i]
            else:
                dp[i] = l[i]
        print(max(dp))
    except:
        break
