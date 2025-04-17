class Node:
    def __init__(self,total:int,start:int,end:int):
        self.left=None
        self.right=None
        self.start=start
        self.end=end 
        self.sum=total

class SegmentTree:

    
    def __init__(self, nums: List[int]):
        self.root=self.build(nums,0,len(nums)-1)
    
    def build(self,nums,start,end):
        if start==end:
            return Node(nums[start],start,end)
        
        m=(start+end)//2
        root=Node(0,start,end)
        root.left=self.build(nums,start,m)
        root.right=self.build(nums,m+1,end)
        root.sum=root.left.sum+root.right.sum
        return root

    
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root,index,val)
    
    def update_helper(self,root,index,val):
        if root.start==root.end:
            root.sum=val
            return

        m=(root.start+root.end)//2
        if index>m:
            self.update_helper(root.right,index,val)
        else:
            self.update_helper(root.left,index,val)

        root.sum=root.left.sum+root.right.sum


    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root,L,R)
    
    def query_helper(self,root,query_start:int,query_end:int):
        if root.start==query_start and root.end==query_end:
            return root.sum
        
        m=(root.start+root.end)//2
        if  query_start > m:
            return self.query_helper(root.right,query_start,query_end)
        elif query_end<=m:
            return self.query_helper(root.left,query_start,query_end)
        else:
            return (self.query_helper(root.left,query_start,m)+self.query_helper(root.right,m+1,query_end))        


