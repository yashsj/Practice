class UnionFind:
    
    def __init__(self, n: int):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n
        self.n_components=n

        
        
        

    def find(self, x: int) -> int:
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]


    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x)==self.find(y)


    def union(self, x: int, y: int) -> bool:
        p1,p2=self.find(x),self.find(y)
        if p1==p2:
            return False
        else:
            if self.rank[p1]>self.rank[p2]:
                self.parent[p2]=p1
            elif self.rank[p2]>self.rank[p2]:
                self.parent[p1]=p2
            else:
                self.parent[p1]=p2
                self.rank[p2]+=1
            self.n_components-=1
        
            return True

    def getNumComponents(self) -> int:
        return self.n_components 

