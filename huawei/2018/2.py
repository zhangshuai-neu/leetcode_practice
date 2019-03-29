def getkey(elem):
    return elem[2]

record = {}
record_list = []
while True:
    try:
        l = input().split('\\')
        nl = l[len(l)-1]
        
        if nl in record:
            num = record[nl]+1
            record.update({nl:num})
        else:
            record.update({nl:1})
            record_list.append(nl)
    except:
        ol = []
        for s in record_list:
            nl_l = s.split()
            name = nl_l[0]
            name = name[-16:]
            line_num = int(nl_l[1])
            count = record[s]
            ol.append([name,line_num,count])
            
        ol.sort(key=getkey,reverse=True)
        for i in range(min(8,len(ol))):
            print(ol[i][0],ol[i][1],ol[i][2])
        break
