# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode = None) -> list[int]:
        def inorder(node, mylist):
            if node:
                if node.left:
                    inorder(node.left, mylist)
                mylist.append(node.val)
                if node.right:
                    inorder(node.right, mylist)
        order = []
        inorder(root, order)
        return order


        
        