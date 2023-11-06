# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(node, prev_depth):
            if not node:
                return prev_depth
            prev_depth += 1
            return max(max_depth(node.left, prev_depth), max_depth(node.right, prev_depth))
        return max_depth(root, 0)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if not (-1 <= l - r <= 1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        