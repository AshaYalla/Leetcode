# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            def solve(node):
                if node == None:
                    return node
                if node.next == None:
                    return node
                h = solve(node.next)
                node.next.next = node
                node.next = None
                return h
            return solve(head)
        
        # # cur = head
        # # prev = None
        # # while(cur):
        # #     nxt = cur.next
        # #     cur.next = prev
        # #     prev = cur
        # #     cur = nxt
        # return prev
        
            
        