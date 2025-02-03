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
        
#DP Bottom-up apprach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
