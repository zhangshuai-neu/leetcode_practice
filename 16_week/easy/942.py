class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        """
        假设我们默认数组中的元素是递增排列的，那么此时影响结果的就是S中的字符‘D’，
        只需要解决字符‘D’对应数组下标位置处的元素，令其符合条件即可；
        我们可以这么做：首先遍历字符串S，每碰到一个字符‘D’时，将当前可分配的元素中的最大值
        赋予数组对应位置处，这样遍历完字符串S后，我们得到的数组就已经解决了字符‘D’的问题，
        这时候，只需要遍历数组将其没有赋值的位置，按照剩余可分配元素从小到大的顺序依次填充即可；
        """
        
        N = len(S)
        max_num = N
        min_num = 0
        A = [0 for i in range(N+1)]
        for i in range(N):
            if S[i]=='D':
                A[i] = max_num
                max_num = max_num-1
        for i in range(N):
            if S[i]=='I':
                A[i] = min_num
                min_num = min_num+1
        A[N]=min_num
        return A
