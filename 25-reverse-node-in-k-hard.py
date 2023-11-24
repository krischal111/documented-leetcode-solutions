# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        stack = []
        myhead = ListNode(0, head)
        prev_group_last = myhead
        node = head
        while node:
            stack.append(node)

            next_node = node.next
            if len(stack) == k:
                localnode = stack.pop()
                prev_group_last.next = localnode
                while stack:
                    localnode.next = stack.pop()
                    localnode = localnode.next
                localnode.next = next_node
                prev_group_last = localnode
            node = next_node
        return myhead.next