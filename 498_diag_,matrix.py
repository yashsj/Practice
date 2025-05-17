class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_dict=defaultdict(list)
        rows,cols=len(mat),len(mat[0])
        for j in range(cols):
            for i in range(rows):
                my_dict[i+j].append(mat[i][j])
        
        res=[]
        for i in range(rows+cols-1):
            if i%2==1:
                res.extend(reversed(my_dict[i]))
            else:
                res.extend(my_dict[i])
        return res
        
