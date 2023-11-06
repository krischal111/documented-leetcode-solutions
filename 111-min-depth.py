# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# include "binary-tree-tool.py"
import binary_tree_tool

class Solution:
    def minDepth(self, root = None) -> int:
        if not root:
            return 0
        queue =  [root]
        queue1 = []
        i = 1
        while queue:
            for node in queue:
                left = node.left
                right = node.right
                if (not left) and (not right):
                    return i+1
                if left:
                    queue1.append(left)
                if right:
                    queue1.append(right)
                
            queue = queue1

testcase = [2,None,3,None,4,None,5,None,6]
tree = binary_tree_tool.make_tree_from_bfs_list(testcase)
print(tree)
print("Another tree is")
testcase = [2, 3, 4, None, 5, None, None, 6, 7]
print(binary_tree_tool.make_tree_from_bfs_list(testcase))

