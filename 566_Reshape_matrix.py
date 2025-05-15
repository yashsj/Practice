class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat=[]
        for row in mat:
            for num in row:
                flat.append(num)
        if len(flat)!=(r*c):
            return mat 
        return [flat[i*c:(i+1)*c] for i in range(r)]
