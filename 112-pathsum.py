class Solution:
    def hasPathSum(self, root, target):
        if root is None:
            print("False coz no leaves")
            return False
        
        val, left, right = root.val, root.left, root.right
        target = target - val
    
        if (left is None) and (right is None): # leaf node
            # print(f"{target == 0} at leaf node {val} with target = {target}")
            return target == 0
        
        condition = False
        if left:
            condition = condition or self.hasPathSum(left, target)
        if right:
            condition = condition or self.hasPathSum(right, target)
        
        return condition
    

import binary_tree_tool
list = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree = binary_tree_tool.make_tree_from_bfs_list(list)
print(tree)

ans = Solution().hasPathSum(tree, 22)
print(ans)
    
    # def hasPathSum(self, root, target):
    #     if root is None:
    #         return False
        
    #     return self.hasmyPathSum(root, target)
