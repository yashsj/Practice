class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]
        n=len(nums)
        def dfs(i):
            if i==n:
                res.append(sol[:])
                return
         
            #exclude the element
            dfs(i+1)
            #include the element
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
        dfs(0)
        return res
