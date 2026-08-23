# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Solution 1 with hashMap
        # hashS = set()
        # while head:
        #     if head in hashS:
        #         return True
        #     else:
        #         hashS.add(head)
        #     head = head.next
        # return False
        
        # Solution 2 with 2 pointers (fast & slow)
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False