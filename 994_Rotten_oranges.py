class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,time=0,0
        rows,cols=len(grid),len(grid[0])
        queue=collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh+=1
                if grid[row][col]==2:
                    queue.append((row,col))
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while queue and fresh>0:
            for i in range(len(queue)):
                rowx,coly=queue.popleft()
                for nr,nc in directions:
                    dr,dc=nr+rowx,coly+nc
                    if dr>=rows or dc>=cols or dr<0 or dc<0 or grid[dr][dc]==0 or grid[dr][dc]==2:
                        continue
                    queue.append((dr,dc))
                    grid[dr][dc]=2
                    fresh-=1
            time=time+1
        return time if fresh==0 else -1
    

