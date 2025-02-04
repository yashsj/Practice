class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[rows-1][cols-1]==1:
            return 0

        dp=[0]*(cols+1)
        dp[cols-1]=1
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if obstacleGrid[r][c]==1:
                    dp[c]=0
                else:
                    dp[c]=dp[c]+dp[c+1]
        return dp[0]  
