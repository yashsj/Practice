class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax,globalmin=nums[0],nums[0]
        curr_max=0
        curr_min=0
        total=0
        for num in nums:
            curr_max=max(num,curr_max+num)
            globalmax=max(curr_max,globalmax)
            curr_min=min(num,curr_min+num)
            globalmin=min(curr_min,globalmin)
            total+=num
        return max(globalmax,total-globalmin) if globalmax>0 else globalmax




        
