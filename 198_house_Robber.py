class Solution:
    def rob(self, nums: List[int]) -> int:
        #Top Down approach
        n=len(nums)
        dp=[0]*n
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
            
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]




class Solution:
    def rob(self, nums: List[int]) -> int:
        #Space optimized version

        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        
        
        prev,curr=nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            prev,curr=curr,max(prev+nums[i],curr)
        return curr

        
