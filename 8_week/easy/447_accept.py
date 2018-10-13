class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
<<<<<<< HEAD
        
        
        
        
        
        
        
        
=======
        all_boomerang_count = 0
        points_num = len(points)
        distance_map = {}
        for i in range(points_num):
            #初始化
            distance_map.clear()
            #统计 point i 到每个点的距离
            for j in range(points_num):
                if j == i:
                    continue
                else:
                    #距离计算结果存入 map 中，用来统计不同距离的次数
                    x = points[i][0]-points[j][0]
                    y = points[i][1]-points[j][1]
                    distance=x*x+y*y
                    if distance not in distance_map:                        
                        distance_map.update({distance:1})
                    else:
                        count = distance_map.get(distance)
                        distance_map[distance] = count+1

            #针对每种距离计算boomerang_count，并存入
            value_list = list(distance_map.values())
            value_list_len = len(value_list)
            for k in range(value_list_len):
                boomerang_count = value_list[k]*(value_list[k]-1)
                #加上 point i 在一种距离下的 boomerang 数
                all_boomerang_count = all_boomerang_count+boomerang_count

        return all_boomerang_count



>>>>>>> bddf464449253baab3c26b689d28795b2911c3c9
