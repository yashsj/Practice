class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        for i in range(n):
            if group[i]==-1:
                group[i]=m
                m+=1

        item_adj=defaultdict(list)
        group_adj=defaultdict(list)
        item_indegree=[0]*n
        group_indegree=[0]*m

        for i in range(n):
            for par in beforeItems[i]:
                item_adj[par].append(i)
                item_indegree[i]+=1
                if group[i]!=group[par]:
                    group_adj[group[par]].append(group[i])
                    group_indegree[group[i]]+=1
        
        itm=self.top_sort(item_adj,item_indegree,n)
        if not itm:
            return []
        grp=self.top_sort(group_adj,group_indegree,m)
        if not grp:
            return []
        grouping=defaultdict(list)
        for i in itm:
            grouping[group[i]].append(i)
        res=[]
        for g in grp:
            res.extend(grouping[g])
        return res

    def top_sort(self,adj,indegree,N):
        topo=[]
        q=deque([i for i in range(N) if indegree[i]==0])
        while q:
            node=q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return topo if len(topo)==N else []


                




            

