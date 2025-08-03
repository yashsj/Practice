class UnionFind:
    def __init__(self,n:int):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n
    
    def find_parent(self,n:int):
        if self.parent[n]!=n:
            self.parent[n]=self.find_parent(self.parent[n])
        return self.parent[n]
    
    def union(self,node1:int,node2:int):
        px,py=self.find_parent(node1),self.find_parent(node2)
        if px!=py:
            if self.rank[px]>self.rank[py]:
                self.parent[px]=py
                self.rank[py]+=self.rank[px]
            else:
                self.parent[py]=px
                self.rank[px]+=self.rank[py]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minheap=[]
        for node1,node2,weight in edges:
            heapq.heappush(minheap,[weight,node1,node2])
        unionfind=UnionFind(n)

        res=0
        components=n
        while components>1 and minheap:
            weight,node1,node2=heapq.heappop(minheap)
            if unionfind.union(node1,node2):
                res+=weight
                components-=1
        return res if components==1 else -1

