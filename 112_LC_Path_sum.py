# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum==root.val

        left_sum=self.hasPathSum(root.left, targetSum-root.val)
        right_sum= self.hasPathSum(root.right, targetSum-root.val)
        return left_sum or right_sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: 
        def dfs(node,total_sum):
            if not node:
                return False
            total_sum+=node.val
            if not node.left and not node.right:
                return total_sum == targetSum
            return (dfs(node.left,total_sum) or dfs(node.right,total_sum))
        return dfs(root,0)
