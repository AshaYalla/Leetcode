
            
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head 
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        prev = None
        while(cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur = head
        while(prev.next):
            nxt = cur.next
            prevnxt = prev.next
            
            cur.next = prev
            prev.next = nxt
            prev = prevnxt
            cur = nxt
  
