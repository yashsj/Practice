class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj={}
        for i in range(n+1):
            adj[i]=[]
        for s,d,w in edges:
            adj[s].append([d,w])

        shortest={}
        minheap=[[0,src]]
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1]=w1

            for n2,w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap,[w2+w1,n2])

        for i in range(n):
            if i not in shortest:
                shortest[i]=-1
        return shortest


