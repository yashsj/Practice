class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #visited=set()
        res=[]
        adj={}
        for i in range(numCourses):
            adj[i]=[]
        for src,dst in prerequisites: 
            adj[src].append(dst)
        def dfs(start,target,visited)->bool:
            if start==target:
                return True
            if start in visited:
                return False
            visited.add(start)


            for nei in adj[start]:
                if dfs(nei,target,visited):
                    return True
            return False
        for start,target in queries:
            visited=set()
            res.append(dfs(start,target,visited))
        return res
