class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0])==1:
            return -1
        rows,cols=len(grid),len(grid[0])
        visited=set()
        visited.add((0,0))
        queue=collections.deque()
        queue.append((0,0))
        path=1
        while queue:
            for i in range(len(queue)):
                row,col=queue.popleft()
                if row==rows-1 and col==cols-1:
                    return path
                directions=[[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]]
                for dr,dc in directions:
                    dr,dc=dr+row,dc+col

                    #find if the grid satisfies all the conditions
                    if (min(dr,dc)<0 or dr==rows or dc==cols or ((dr,dc)) in visited or grid[dr][dc]==1):
                        continue
                    queue.append((dr,dc))
                    visited.add((dr,dc))
            path=path+1  
        return -1

