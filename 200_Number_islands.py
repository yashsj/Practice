class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        ROWS,COLS=len(grid),len(grid[0])
        visited=set()

        
        def dfs(row,col):
            if (row<0 or row==ROWS or col<0 or col==COLS or (row,col) in visited or grid[row][col]=="0"):
                return 
            visited.add((row,col))
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)

        
        for row in range(ROWS):
            for col in range(COLS):
                
                if grid[row][col]=="1" and (row,col) not in visited:
                    dfs(row,col)
                    count+=1
        return count


        
