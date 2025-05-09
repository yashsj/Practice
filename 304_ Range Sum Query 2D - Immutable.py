class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])
        self.sum_Matrix=[[0]*(cols+1) for _ in range(cols+1)]
        for row in range(rows):
            for col in range(cols):
                self.sum_Matrix[row+1][col+1]=matrix[row][col]+self.sum_Matrix[row+1][col]+self.sum_Matrix[row][col+1]-self.sum_Matrix[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_Matrix[row2+1][col2+1]-self.sum_Matrix[row1][col2+1]-self.sum_Matrix[row2+1][col1]+self.sum_Matrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
