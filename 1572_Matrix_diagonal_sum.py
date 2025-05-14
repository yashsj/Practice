class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        side=len(mat)
        ans=0
        for i in range(side):
                ans+=mat[i][i]
                ans+=mat[side-i-1][i]
        if side%2==1:
            ans-=mat[side//2][side//2]
        return ans
