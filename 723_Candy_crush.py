class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows,cols=len(board),len(board[0])
        crushed=False

        #HorizontalCheck
        for i in range(rows):
            for j in range(cols-2):
                if abs(board[i][j])==abs(board[i][j+1])==abs(board[i][j+2]) !=0:
                    board[i][j]=board[i][j+1]=board[i][j+2]=-abs(board[i][j])
                    crushed=True

        #VerticalCheck
        for i in range(rows-2):
            for j in range(cols):
                if abs(board[i][j])==abs(board[i+1][j])==abs(board[i+2][j]) !=0:
                    board[i][j]=board[i+1][j]=board[i+2][j]=-abs(board[i][j])
                    crushed=True
        #crush

        for j in range(cols):
            limit=rows-1
            for i in range(rows-1,-1,-1):
                if board[i][j]>0:
                    board[limit][j]=board[i][j]
                    limit-=1

            for i in range(limit+1):
                board[i][j]=0
        return self.candyCrush(board) if crushed else board        

