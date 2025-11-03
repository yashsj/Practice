class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        hashmap={}
        minheap=[]
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for num in hashmap.keys():
            heapq.heappush(minheap,(hashmap[num],num))
            if len(minheap)>k:
                heapq.heappop(minheap)
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
