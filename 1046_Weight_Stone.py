class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[-stone for stone in stones]
        #use a min heap 
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            x=heapq.heappop(maxheap)
            y=heapq.heappop(maxheap)
            if y>x:
                heapq.heappush(maxheap,x-y)
        maxheap.append(0)
        return abs(maxheap[0])
