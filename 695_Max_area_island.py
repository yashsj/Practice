class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        max_area=0
        visited=set()
        def dfs(row,col):
            if (row<0 or col <0 or row==rows or col==cols or grid[row][col]==0 or (row,col) in visited):
                return 0
            visited.add((row,col))
            return(1+ dfs(row+1,col)+dfs(row-1,col)+dfs(row,col+1)+dfs(row,col-1))

        for row in range(rows):
            for col in range(cols):
                if ((row,col) not in visited and grid[row][col]==1):
                    max_area=max(max_area,dfs(row,col))
                    visited.add((row,col))
            
        return max_area


            
        
