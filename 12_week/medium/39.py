class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 从candinate中取一个数字，压入global_stack中
        # 如果小于target,可以尝试压入index索引之后的数字(包括index)
        # 如果大于等于target,退回
        def get(combination_list, candidates, target, global_stack, index):
            if len(global_stack)==0 or sum(global_stack)<target:
                for i in range(index,len(candidates)):
                    global_stack.append(candidates[i])
                    get(combination_list, candidates, target, global_stack, i)
                    global_stack.pop()
                return 

            if sum(global_stack)>=target:
                if sum(global_stack)==target:
                    combination_list.append(global_stack.copy())
                return

        combination_list = []
        candidates.sort()
        global_stack = []

        get(combination_list, candidates, target, global_stack, 0)
        print(combination_list)

        return len(combination_list)
