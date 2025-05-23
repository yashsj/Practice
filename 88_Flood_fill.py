class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        org=image[sr][sc]
        def dfs(row,col):
            if not(0<=row<rows and 0<=col<cols):
                return
            if image[row][col]!=org:
                return
            image[row][col]=color
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        if org!=color:
            dfs(sr,sc)
        return image

        
