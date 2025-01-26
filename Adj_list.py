class Graph:
    
    def __init__(self):
        self.adj_list={}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src]=set()
        if dst not in self.adj_list:
            self.adj_list[dst]=set()
        self.adj_list[src].add(dst)



    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True 


    def hasPath(self, src: int, dst: int) -> bool:
        queue=collections.deque()
        visited=set()
        queue.append(src)
        while queue:
                node=queue.popleft()
                if node==dst:
                    return True
                visited.add(node)
                for n in self.adj_list.get(node,[]):
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
        return False





