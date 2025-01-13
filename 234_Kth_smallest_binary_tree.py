class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums=[]

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)
        return nums[k-1]
