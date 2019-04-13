# 将 num 拆成 s份
global_list = [·]
def cut(pre_val,num, s):
    if num<s:
        return []
    if num==s:
        result = []
        if pre_val<=1:
            result.append([1 for i in range(num)])
        return result
    # num > s
    result = []
    if s==1:
        if num>=pre_val:
            result.append([num])
        return result

    for i in range(pre_val, num):
        ret_list = cut(i,num-i, s-1) 
        for l in ret_list:
            l.insert(0,i)
        result.extend(ret_list)
    return result

# 10 拆成3份，起始值要大于等于1
ret = cut(1,10,3)
print(ret)
