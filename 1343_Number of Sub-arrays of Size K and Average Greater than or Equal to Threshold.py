class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        curr_sum=sum(arr[:k-1])
        for R in range(len(arr)-k+1):
            curr_sum+=arr[R+k-1]
            if (curr_sum/k)>=threshold:
                ans+=1
            curr_sum-=arr[R]
        return ans

