# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def areMirrors(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p) ^ (not q):
            return False
        if p.val != q.val:
            return False
        if self.areMirrors(p.left, q.right):
            return self.areMirrors(p.right, q.left)
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if (not root.left) ^ (not root.right):
            return False
        if (not root.left) and (not root.right):
            return True
        return self.areMirrors(root.left, root.right)

                   