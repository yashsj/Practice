class Node:
    def __init__(self,key:int,value:int):
        self.key=key
        self.value=value
        self.next=None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.next=None
        self.prev=None
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
        self.cache={}
    
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=node
        nxt.prev=node
        node.next,node.prev=nxt,prev

    

    def delete(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev



    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.delete(lru)
            del self.cache[lru.key]
       




        
