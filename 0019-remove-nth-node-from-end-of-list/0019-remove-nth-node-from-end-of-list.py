# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        
        
        while(n):
            cur = cur.next
            n = n - 1
        nnode = head
        if not cur:
            head = head.next
        else:
            while(cur):
                prev = nnode
                nnode = nnode.next
                cur = cur.next
            prev.next = nnode.next
        
        return head
            
        