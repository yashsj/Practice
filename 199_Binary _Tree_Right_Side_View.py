class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=collections.deque()
        q.append(root)
        ans=[]
        while q:
            
            rightside=None
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if node:
                    rightside=node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                ans.append(rightside.val)
        return ans
                
