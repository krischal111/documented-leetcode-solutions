# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        this = head
        carry = 0
        while l1 or l2:
            d1 = 0
            d2 = 0
            if l1 is not None:
                d1 = l1.val
                l1 = l1.next
            if l2 is not None:
                d2 = l2.val
                l2 = l2.next
            sum = d1 + d2 + carry
            this.next = ListNode(sum % 10)
            this = this.next
            carry = sum // 10
        if carry:
            this.next = ListNode(carry)

        return head.next
                
        