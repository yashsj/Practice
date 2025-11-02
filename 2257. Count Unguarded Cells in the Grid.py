class Solution:
    UNGUARDED=0
    GUARDED=1
    GUARD=2
    WALL=3

    def dfs(self,r:int,c:int,grid:List[List[int]],direction:str):
        if(r<0 or r>=len(grid) or 
        c<0 or c>=len(grid[0]) or 
        grid[r][c]==self.GUARD  or 
        grid[r][c]==self.WALL):
            return 
        grid[r][c]=self.GUARDED # Make the cells as GUARDED
        if direction=="U":
            self.dfs(r-1,c,grid,"U")
        elif direction=="D":
            self.dfs(r+1,c,grid,"D")
        elif direction=="L":
            self.dfs(r,c-1,grid,"L")
        else:
            self.dfs(r,c+1,grid,"R")
    


    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        #make the grid first and mark all the cells as unguarded by default
        grid=[[self.UNGUARDED]*n for _ in range(m)]

        for guard in guards:
            grid[guard[0]][guard[1]]=self.GUARD

        #mark the walls as well
        for wall in walls:
            grid[wall[0]][wall[1]]=self.WALL
        
        #Now lets use dfs on every guard cell since thats where we can mark the cells that are guarded and we cannot use it for counting purposes 
        for guard in guards:
            self.dfs(guard[0]-1,guard[1],grid,"U")
            self.dfs(guard[0]+1,guard[1],grid,"D")
            self.dfs(guard[0],guard[1]-1,grid,"L")
            self.dfs(guard[0],guard[1]+1,grid,"R")
        
        ans=sum(row.count(self.UNGUARDED) for row in grid)
        return ans



        
