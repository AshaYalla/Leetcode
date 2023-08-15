# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        prev = None
        while(cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        slow.next = None
        cur = head
        while(prev):
            nxt = prev.next
            anxt = cur.next
            cur.next = prev
            prev.next = anxt
            prev = nxt
            cur = anxt
        

         


        