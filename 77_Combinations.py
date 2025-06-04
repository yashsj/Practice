class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        curSet=[]
        self.helper(1,curSet,res,n,k)
        return res
    def helper(self,i,curSet,res,n,k):
        if len(curSet)==k:
            res.append(curSet.copy())
            return 
        if i>n:
            return 
        curSet.append(i)
        self.helper(i+1,curSet,res,n,k)
        curSet.pop()

        self.helper(i+1,curSet,res,n,k)
