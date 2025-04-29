class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])
        return res
        
        
