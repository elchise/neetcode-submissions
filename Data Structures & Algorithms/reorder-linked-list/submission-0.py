# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prv = None
        slow.next = None
        while second:
            tmp = second.next
            second.next = prv
            prv = second
            second = tmp
        
        beg = head
        end = prv
        while end:
            tmp1, tmp2 = beg.next, end.next
            beg.next = end
            end.next = tmp1
            beg = tmp1
            end = tmp2
            
        

        

        