class UnionFind:
    def __init__(self,n:int):
        self.rank=[1]*n
        self.parent=[i for i in range(n)]
    
    def find_parent(self,x:int)->int:
        if x!=self.parent[x]:
            self.parent[x]=self.find_parent(self.parent[x])
        return self.parent[x]
    
    def union(self,node1:int,node2:int)->bool():
        px,py=self.find_parent(node1),self.find_parent(node2)
        if px!=py:
            if self.rank[px]>self.rank[py]:
                self.parent[py]=px
                self.rank[px]+=self.rank[py]
            else:
                self.parent[px]=py
                self.rank[py]+=self.rank[px]
            return True
        return False
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical=[]
        pseudo=[]
        for i,e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda e:e[2])
        mst_weight=0
        uf=UnionFind(n)
        for v1,v2,w,i in edges:
            if uf.union(v1, v2):
                mst_weight+=w
        for n1,n2,e_weight,i in edges:
            weight=0
            uf=UnionFind(n)
            for v1,v2,w,j in edges:
                if i!=j and uf.union(v1,v2):
                    weight+=w
            if max(uf.rank)!=n or weight >mst_weight:
                critical.append(i)
                continue
            uf=UnionFind(n)
            uf.union(n1,n2)
            weight=e_weight
            for v1,v2,w,j in edges:
                if uf.union(v1,v2):
                    weight+=w
            if weight==mst_weight:
                pseudo.append(i)
        return [critical,pseudo]




