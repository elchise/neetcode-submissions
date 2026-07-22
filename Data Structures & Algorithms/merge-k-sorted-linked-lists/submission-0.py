# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l, r = 0, (len(lists)-1)
        
        def divide(lists, l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]

            mid = (l + r) // 2
            left = divide(lists, l, mid)
            right = divide(lists, mid+1, r)
            return merge(left, right)
            

        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy

            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            
            while l1 is not None:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            
            while l2 is not None:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
                
            return dummy.next
        
        return divide(lists, l, r)


