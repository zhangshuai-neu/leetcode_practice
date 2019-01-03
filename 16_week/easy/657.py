class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        moves_len = len(moves)
        for i in range(moves_len):
            if moves[i] =='U':
                y=y+1
                continue
            if moves[i] =='D':
                y=y-1
                continue
            if moves[i] =='L':
                x=x-1
                continue
            if moves[i] =='R':
                x=x+1
                continue
                
        if x==0 and y==0:
            return True
        else:
            return False
