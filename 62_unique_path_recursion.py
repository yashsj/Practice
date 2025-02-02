class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows=m
        cols=n
        #cache=[[0]* for _ in range(cols)]
        def dfs(r,c):
            if r==rows or c==cols:
                return 0
            if r==rows-1 and c==cols-1:
                return 1
            
            return dfs(r+1,c)+dfs(r,c+1)

        return dfs(0,0)
            #cache[r][c]=
        
