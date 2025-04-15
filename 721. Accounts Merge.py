class UnionFind:
    def __init__(self,n):
        self.rank=[1]*n
        self.parent=[i for i in range(n)]
    
    def find(self,node):
        if node!=self.parent[node]:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,n1,n2):
        node1,node2=self.find(n1),self.find(n2)
        if node1==node2:
            return False

        else:
            if self.rank[node1]>self.rank[node2]:
                self.parent[node2]=node1
            elif self.rank[node2]>self.rank[node1]:
                self.parent[node1]=node2
            else:
                self.parent[node1]=node2
                self.rank[node2]+=1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}  # email -> index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)  # index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = [accounts[i][0]]
            name.extend(sorted(emails))
            res.append(name)
        return res



            

        




        
