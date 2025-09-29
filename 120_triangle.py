class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for row in range(1,len(triangle)):
            for col in range(row+1):
                small=math.inf
                if col>0:
                    small=triangle[row-1][col-1]
                if row>col:
                    small=min(triangle[row-1][col],small)
                triangle[row][col]+=small
        return min(triangle[-1])
                    
