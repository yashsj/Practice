class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side=len(matrix)
        left=0
        right=side-1
        while left<right:
            matrix[left],matrix[right]=matrix[right],matrix[left]
            left+=1
            right-=1
        
        for row in range(side):
            for col in range(row,side):
                matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
        
        

        



                

        
        
