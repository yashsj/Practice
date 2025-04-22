class Node(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.total=0
        self.left=None
        self.right=None
    
        

class NumArray(object):

    def __init__(self,nums):
        def createTree(nums,l,r):
            
            if l==r:
                n=Node(l,r)
                n.total=nums[l]
                return n
            
            mid=(l+r)//2
            root=Node(l,r)

            root.left=createTree(nums,l,mid)
            root.right=createTree(nums,mid+1,r)
            root.total=root.left.total+root.right.total
            return root
        self.root=createTree(nums,0,len(nums)-1)

    def update(self,index,val):
        def updateTree(root,index,val):
            if root.start==root.end:
                root.total=val
                return val
            mid=(root.start+root.end)//2

            if index<=mid:
                updateTree(root.left,index,val)
            else:
                updateTree(root.right,index,val)
            root.total=root.left.total+root.right.total
            return root.total 
        return updateTree(self.root,index,val)




    def sumRange(self, i, j):
        def rangeSum(root,i,j):
            if root.start== i and root.end==j:
                return root.total


            mid=(root.start+root.end)//2

            if j<=mid:
                return rangeSum(root.left,i,j)
            elif i>=mid+1:
                return rangeSum(root.right,i,j)
            else:
                return rangeSum(root.left,i,mid)+rangeSum(root.right,mid+1,j)
        return rangeSum(self.root, i, j)


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
