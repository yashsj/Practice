class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS,COLS=len(matrix),len(matrix[0])
        dp=[[0]*(COLS+1) for _ in range(ROWS+1)]
        ans=0
        for row in range(ROWS-1,-1,-1):
            for col in range(COLS-1,-1,-1):
                if matrix[row][col]=="1":
                    dp[row][col]=1+min(dp[row+1][col],dp[row][col+1],dp[row+1][col+1])
                ans=max(ans,dp[row][col])
        return ans*ans
