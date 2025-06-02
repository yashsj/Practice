class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,current_subset=[],[]
        nums.sort()
        self.dfs(0,nums,current_subset,res)
        return res
        
    
    def dfs(self,i,nums,current_subset,res):
        if i==len(nums):
            res.append(current_subset.copy())
            return
        else:
            #include the next char
            current_subset.append(nums[i])
            self.dfs(i+1,nums,current_subset,res)
            current_subset.pop()

            #Not to inlcude the next char
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            self.dfs(i+1,nums,current_subset,res)
            
        
