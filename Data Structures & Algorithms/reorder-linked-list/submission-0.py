# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        cur = head
        mid = head
        
        if not head or not head.next:
            return
        # Find the midpoint 
        while cur and cur.next:
            mid = mid.next
            cur = cur.next.next
        
        # Separate the lists       
        second = mid.next
        mid.next = None

        # Reverse the second half of the list
        
        prev = None
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode
        
        
        
        
        # Merge the lists together
        first = head
        second = prev
        while second:
            firstNext =first.next
            secondNext = second.next

            first.next = second
            second.next =firstNext

            first =firstNext
            second = secondNext





