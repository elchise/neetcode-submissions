# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        while n > 0:
            end = end.next
            n -= 1
        
        beg = dummy = ListNode(0, head)
        while end:
            beg = beg.next
            end = end.next

        beg.next = beg.next.next
        return dummy.next