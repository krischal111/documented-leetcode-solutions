class Solution:
    def zigzagLevelOrder(self, root):
        queuequeue = []
        if not root:
            return queuequeue
        queue = [root]
        nextqueue = []
        
        zigzag = True 
        while queue:
            zigzag = not zigzag
            valqueue = []
            for node in queue:
                left, right = node.left, node.right
                if left:
                    nextqueue.append(left)
                if right:
                    nextqueue.append(right)
                valqueue.append(node.val)
            
            if zigzag:
                valqueue = valqueue[::-1]
            
            queue = list(nextqueue)
            nextqueue = []
            queuequeue.append(valqueue)
        
        return queuequeue
    