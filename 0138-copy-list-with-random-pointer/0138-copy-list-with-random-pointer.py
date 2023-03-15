"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
    

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        dictt = {None:None}
        cur = head
        
        root = Node(cur.val, None,None)
        new = root
        
        while(cur):
            new.next = Node(cur.val, None,cur.random)
            dictt[cur] = new.next
            cur = cur.next
            new = new.next
            
        cur = root.next
        while(cur):
            cur.random = dictt[cur.random]
            cur = cur.next
            
        return root.next
            
        
            
            
        
            
        