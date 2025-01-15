class TreeNode:
     def __init__(self,key:int,val:int):
        self.val=val
        self.key=key
        self.left=None
        self.right=None

class TreeMap:
    def __init__(self,key:int,val:int):
        self.root=None


    def insert(self, key: int, val: int) -> None:
        node=TreeNode(key,val)
        if self.root==None:
            self.root=node
            return
        current=self.root
        while True:
            if key<current.key:
                if current.left==None:
                    current.left=node
                    return
                current=current.left
            elif key>current.key:
                if current.right==None:
                    current.right=node
                    return
                current=current.right
            else:
                current.val=val
                return
                

    def get(self, key: int) -> int:
        current=self.root
        while current!=None:
            if key<current.key:
                current=current.left
            elif key>current.key:
                current=current.right
            else:
                return current.val
        return -1


    def getMin(self) -> int:
        current=self.root
        return current.val if current else -1
    def findmin(self,node:TreeNode)-> TreeNode:
        while node and node.left:
            node=node.left 
        return node


    def getMax(self) -> int:
        current=self.root
        while current and current.right:
            current=current.right
        return current.val if current else -1


    def remove(self, key: int) -> None:
        self.root=self.removehelper(self.root,key)

    def removehelper(self,curr:TreeNode,key:int)->TreeNode:
        if curr==None:
            return None
        if key>curr.key:
            curr.right=self.removehelper(curr.right,key)
        elif key<curr.key:
            curr.left=self.removehelper(curr.left,key)
        else:
            if curr.left==null:
                return curr.right 
            elif curr.right==null:
                return curr.left 
            else:
                minNode=self.findmin(curr.right)
                curr.key=minnode.key
                curr.val=minnode.val
                curr.right=self.remove(curr.right,minnode.key)
            return curr


    def getInorderKeys(self) -> List[int]:
        result=[]
        self.inorderTr(self.root,result)
        return result

    def inorderTr(self,root:TreeNode,result:List[int])->None:
        if root!=None:
            self.inorderTr(root.left,result)
            result.append(root.key)
            self.inorderTr(root.right,result)

