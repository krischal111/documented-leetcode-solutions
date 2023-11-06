# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        cur = head
        already = set()
        skip = ListNode()
        while cur:
            val = cur.val
            if val not in already:
                already.add(val)
                skip.next = cur
                skip = cur
                pass
            cur = cur.next
        skip.next = None
        return head