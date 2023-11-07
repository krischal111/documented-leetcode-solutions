class Solution:
    def levelOrder(self, root):
        queuequeue = []
        if not root:
            return queuequeue
        queue = [root]
        nextqueue = []
        
        while queue:
            valqueue = []
            for node in queue:
                left, right = node.left, node.right
                if left:
                    nextqueue.append(left)
                if right:
                    nextqueue.append(right)
                valqueue.append(node.val)
            
            queue = list(nextqueue)
            nextqueue = []
            queuequeue.append(valqueue)
        
        return queuequeue
    