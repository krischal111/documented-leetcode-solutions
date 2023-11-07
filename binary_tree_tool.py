# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        def printnode(node, depth):
            if node is None:
                return ''
            s = printnode(node.left, depth+1)
            s += f"{'    ' if depth else ''}{'   |'*(depth-1)}   +---{node.val}\n"
            s += printnode(node.right, depth+1)
            return s

        return "\n"+printnode(self, 0)

from collections import deque

def make_tree_from_bfs_list(tree_array):
    queue = deque(tree_array)
    if not queue:
        return None
    
    head = TreeNode(queue.popleft())
    nodequeue = deque([head])
    while queue:
        left = queue.popleft()
        right = queue.popleft()
        if left is not None:
            left = TreeNode(left)
            nodequeue.append(left)
        if right is not None:
            right = TreeNode(right)
            nodequeue.append(right)
        node = nodequeue.popleft()
        node.left = left
        node.right = right
    
    return head

def make_bfs_list_from_bst(head):
    if head is None:
        return []
    
    bfslist = []
    queue = deque([head])
    while queue:
        node = queue.popleft()
        nodeval = None
        if node is not None:
            nodeval = node.val
            queue.append(node.left)
            queue.append(node.right)
        bfslist.append(nodeval)
    return bfslist

if __name__ == '__main__':
    array = [3, 9, 20, None, None, 15, 7]
    for _ in range(1):
        print("Bfs Array = ", array)
        tree = make_tree_from_bfs_list(array)
        print("Tree from bfs ")
        print(str(tree))
        # print(tree)
        array = make_bfs_list_from_bst(tree)
        print("Bfs from tree = ", array)

    print()
    testcase = [2, 3, 4, None, 5, None, None, 6, 7]
    print(testcase)
    print(make_tree_from_bfs_list(testcase))
        
            
            
        
    
    
        