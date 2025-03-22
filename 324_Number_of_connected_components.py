class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents=[i for i in range(n)]
        rank=[1]*(n)
        n_components=n

        def find(node):
            if parents[node]!=node:
                parents[node]=find(parents[node])
            return parents[node]

        def union(node1,node2):
            nonlocal n_components
            n1,n2=find(node1),find(node2)
            if parents[n1]==parents[n2]:
                return False
            else:
                if rank[n1]>rank[n2]:
                    parents[n2]=n2
                elif rank[n2]>rank[n1]:
                    parents[n1]=n2
                else:
                    parents[n1]=n2
                    rank[n1]+=1
                n_components-=1
                return True

        for a,b in edges:
            union(a,b)
        return n_components