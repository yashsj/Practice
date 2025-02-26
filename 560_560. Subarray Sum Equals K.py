class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum={0:1}
        ans=0
        res=0
        for num in nums: 
            res+=num
            if res-k in prefix_sum:
                ans+=prefix_sum[res-k]
            prefix_sum[res]=1+prefix_sum.get(res,0)
        return ans
        
