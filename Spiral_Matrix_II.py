class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top,bottom=0,n-1
        left,right=0,n-1
        value=1
        res=[[0] * (n) for _ in range(n)]
        while left<=right:
            for i in range(left,right+1):
                res[top][i]=value
                value+=1
            top+=1
            for i in range(top,bottom+1):
                res[i][right]=value
                value+=1
            right-=1
            
            for i in range(right,left-1,-1):
                res[bottom][i]=value
                value+=1
            bottom-=1

            for i in range(bottom,top-1,-1):
                res[i][left]=value
                value+=1
            left+=1
        return res

    
