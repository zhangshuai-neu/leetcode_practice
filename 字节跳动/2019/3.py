case_num = int(input())
while True:
    try:
        n = int(input())
        gl = list(map(int,input().split()))
        cl = [0 for i in range(n)]
        min_gl = min(gl)
        for i in range(n):
             if gl[i]<=gl[(i+1)%n] and gl[i]<=gl[(n+i-1)%n]:
                cl[i] = 1
        # 修改count list
        flag=True
        while flag:
            flag = False
            for i in range(n):
                if gl[(i+1)%n]==0 and gl[(n+i-1)%n]==0:
                    continue
                # 最大
                if gl[i]>gl[(i+1)%n] and gl[i]>gl[(n+i-1)%n]:
                    if cl[i]!=max(cl[(i+1)%n],cl[(n+i-1)%n])+1:
                        cl[i] = max(cl[(i+1)%n],cl[(n+i-1)%n])+1
                        flag=True
                if gl[i]<=gl[(i+1)%n] and gl[i]>gl[(n+i-1)%n]:
                    if cl[i] != cl[(n+i-1)%n]+1:
                        cl[i] = cl[(n+i-1)%n]+1
                        flag=True
                if gl[i]>gl[(i+1)%n] and gl[i]<=gl[(n+i-1)%n]:
                    if cl[i] != cl[(i+1)%n]+1:
                        cl[i] = cl[(i+1)%n]+1
                        flag=True
        print(sum(cl))
    except:
        break
