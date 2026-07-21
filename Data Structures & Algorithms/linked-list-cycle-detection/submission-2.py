# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        hare = head

        while hare and hare.next:


            cur = cur.next
            hare = hare.next.next
            if hare == cur:
                return True
        return False
