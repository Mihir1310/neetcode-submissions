# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = head
        # if n==1 and not r.next:
        #     return head.next
        for _ in range(n):
            r = r.next
        if r is None:
            return head.next
        
        while r and r.next:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return head
