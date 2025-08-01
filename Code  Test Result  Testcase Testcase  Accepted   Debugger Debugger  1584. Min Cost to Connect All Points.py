class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj={}
        N=len(points)
        for i in range(N):
            adj[i]=[]
        for i in range(N):
            x1,y1=points[i]
            for j in range(i+1,N):
                x2,y2=points[j]
                dist=abs(x2-x1)+abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        visited=set()
        minheap=[[0,0]]
        ans=0
        while len(visited)<N:
            weight,node=heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            ans+=weight
            for wei,nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap, [wei,nei])
        return ans
