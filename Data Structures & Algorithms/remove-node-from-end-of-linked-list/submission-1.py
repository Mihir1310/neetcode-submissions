# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        c = 0
        while curr:
            curr = curr.next
            c += 1
        if c == n:
            return head.next
        
        target = c-n
        c = 0
        curr = head
        while curr:
            c += 1
            if c == target:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head      