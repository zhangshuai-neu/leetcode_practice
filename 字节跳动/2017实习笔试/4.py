"""
时间限制：1秒

空间限制：32768K

给定 x, k ，求满足 x + y = x | y 的第 k 小的正整数 y 。 | 是二进制的或(or)运算，例如 3 | 5 = 7。

比如当 x=5，k=1时返回 2，因为5+1=6 不等于 5|1=5，而 5+2=7 等于 5 | 2 = 7。


输入描述:
每组测试用例仅包含一组数据，每组数据为两个正整数 x , k。 满足 0 < x , k ≤ 2,000,000,000。


输出描述:
输出一个数y。


输入例子1:
5 1

输出例子1:
2
"""
while True:
    try:
        x,k = input().split()
        x = int(x)
        k = int(k)
        # 分析bit，y中不能包含x的bit位
        k_bin_l = list(bin(k)[2:])
        x_bin_l = list(bin(x)[2:])
        i = len(x_bin_l)-1
        j = len(k_bin_l)-1
        while i>=0:
            if x_bin_l[i]=='0':
                if j>=0:
                    x_bin_l[i]=k_bin_l[j]
                    j=j-1
            i=i-1
        l = j
        while l>=0:
            x_bin_l.insert(0,k_bin_l[l])
            l=l-1
        y = int("".join(x_bin_l),2)-x
        print(y)
    except:
        break
