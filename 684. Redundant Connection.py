class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)

        def find(n):
            if n!=parent[n]:
                parent[n]=find(parent[n])
            return parent[n]
        
        def union(node1,node2):
            n1,n2=find(node1),find(node2)
            if parent[n1]==parent[n2]:
                return False
            else:
                if rank[n1]>rank[n2]:
                    parent[n2]=n2
                elif rank[n2]>rank[n1]:
                    parent[n1]=n2
                else:
                    parent[n1]=n2
                return True 
            
        for a,b in edges:
            if not union(a,b):
                return [a,b]
            

        
