class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=set()
        path=set()
        n=numCourses
        adj={}
        topsort=[]
        for i in range(n):
            adj[i]=[]        
        for src,dst in prerequisites:
            adj[src].append(dst)
        
        def dfs(n)->bool:
            if n in visited:
                return True 
            if n in path:
                return False
            path.add(n)
            for nei in adj[n]:
                if not dfs(nei):
                    return False
            path.remove(n)
            visited.add(n)
            topsort.append(n)
            return True
        for i in range(n):
            if not dfs(i):
                return []
        
        return topsort
