class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums=[]
        self.dfs(root,nums)
        return nums

    def dfs(self,root,nums):
        if not root:
            return 
        self.dfs(root.left,nums)
        nums.append(root.val)
        self.dfs(root.right,nums)
        
