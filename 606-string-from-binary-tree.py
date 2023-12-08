# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ""
        if not root:
            return string
        string += str(root.val)
        string += '('
        string += self.tree2str(root.left)
        string += ')('
        string += self.tree2str(root.right)
        string += ')'
        while string[-2:] == '()':
            string = string[:-2]
        return string
        