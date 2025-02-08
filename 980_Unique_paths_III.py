class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        ex,ey,sx,sy,empty=0,0,0,0,1
        visited=set()
        result=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    sx=r
                    sy=c
                elif grid[r][c]==0:
                    empty+=1
                elif grid[r][c]==2:
                    ex,ey=r,c
        def dfs(r,c,empty,visited):
            if r<0 or c<0 or r==rows or c==cols or grid[r][c]==-1 or (r,c) in visited:
                return 0
            
            if grid[r][c]==2:
                if empty==0:
                    return 1 
                return 0
            visited.add((r,c))
            empty-=1
            result=(dfs(r+1,c,empty,visited)+
            dfs(r-1,c,empty,visited)+
            dfs(r,c+1,empty,visited)+
            dfs(r,c-1,empty,visited))
            empty=empty+1

            visited.remove((r,c))
            return result
        return dfs(sx,sy,empty,set())

