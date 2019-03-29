import itertools

all_list = list(itertools.permutations([0,1,2,3,4]))
all_len = len(all_list)

def getval(data, p):
    s = 0
    cur_x = 0.0
    cur_y = 0.0
    for i in range(5):
        next_x = data[p[i]*2]
        next_y = data[p[i]*2+1]
        s = s + pow((next_x-cur_x)**2 + (next_y-cur_y)**2, 0.5)
        cur_x = next_x
        cur_y = next_y
    s = s + pow((cur_x-0)**2 + (cur_y-0)**2,0.5)
    return s
    
while True:
    try:
        in_data = list(map(int,input().split()))
        min_val = 100000000000000000000
        for i in range(all_len):
            min_val = min(min_val, getval(in_data, all_list[i]))
        print(int(min_val))
        
    except:
        break
