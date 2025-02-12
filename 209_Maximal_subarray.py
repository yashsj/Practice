class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum=0
        ans=float('inf')
        left=0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                curr_sum-=nums[left]
                ans=min(ans,right-left+1)
                left+=1
        return 0 if ans==float('inf') else ans
               
