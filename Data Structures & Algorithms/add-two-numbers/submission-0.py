# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        carry = 0
        dummy = ListNode()
        cur = dummy
        while n1 or n2 or carry:
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
        
        return dummy.next

        

        