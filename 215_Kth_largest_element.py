class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-n for n in nums]
        heapq.heapify(nums)
        while k>1:
            heapq.heappop(nums)
            k=k-1
        return -1*(heapq.heappop(nums))
        
