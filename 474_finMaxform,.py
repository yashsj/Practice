
#usins the most brute force O(2^n) Goal is just to understand and solution that just works for a few TCs 
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr=[[0]*2 for _ in range(len(strs))]
        for i,s in enumerate(strs):
            for c in s:
                arr[i][ord(c)-ord('0')]+=1

        def dfs(i,m,n):
            if i==len(strs):
                return 0
            res= dfs(i+1,m,n)

            if m>=arr[i][0] and n>=arr[i][1]:
                res=max(res,1+dfs(i+1,m-arr[i][0],n-arr[i][1]))
            return res
        return dfs(0,m,n)
