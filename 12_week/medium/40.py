class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 判断list是否相同
        def is_same_list(l1, l2):
            l1_len = len(l1)
            l2_len = len(l2)
            if l1_len == l2_len:
                for i in range(l1_len):
                    if l1[i] != l2[i]:
                        return False
            else:
                return False
            return True
            
        # 从index之后寻找一个元素
        def get(combination_list, global_stack, candidates, target, index):
            sum_global_stack = sum(global_stack)
            len_candidates = len(candidates)
            
            # 从index之后的元素开始插入
            if sum_global_stack<target:
                for i in range(index, len_candidates):
                    # 插入新元素
                    global_stack.append(candidates[i]);
                    
                    # 过大或相等
                    if sum_global_stack+candidates[i] >= target:
                        if sum_global_stack+candidates[i] == target:
                            sign = False
                            len_combination_list = len(combination_list)
                            for j in range(len_combination_list):
                                if is_same_list(combination_list[j], global_stack):
                                    sign = True
                            if sign==False:
                                combination_list.append(global_stack.copy())
                            
                        global_stack.pop() # 恢复原状
                        break
                        
                    # 不够大，继续插入
                    get(combination_list, global_stack, candidates, target, i+1)
                    
                    # 恢复原状
                    global_stack.pop()
                return
                
        combination_list = []
        candidates.sort()
        global_stack = []
        get(combination_list, global_stack, candidates, target, 0)
        
        return combination_list
