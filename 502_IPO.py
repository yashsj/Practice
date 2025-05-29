class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap=[]
        min_heap=[(cap,pro) for cap,pro in zip(capital,profits)]
        heapq.heapify(min_heap)
        for i in range(k):
            while min_heap and min_heap[0][0]<=w:
                c,p=heapq.heappop(min_heap)
                heapq.heappush(max_heap,-p)
            if not max_heap:
                break
            w+=-heapq.heappop(max_heap)
        return w 
        
