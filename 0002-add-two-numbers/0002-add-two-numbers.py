# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        new = head
        carry = 0
        while(l1 and l2):
            new.next = ListNode((l1.val + l2.val+ carry)%10)
            carry = (l1.val + l2.val+carry)//10
            
            l1 = l1.next
            l2 = l2. next
            new = new.next
        
        while(l1 or l2):
            if(l1):
                new.next = ListNode((l1.val + carry)%10)
                carry = (l1.val + carry)//10
                l1 = l1.next
                new = new.next
            else:
                new.next = ListNode((l2.val + carry)%10)
                carry = (l2.val + carry)//10
                l2 = l2.next
                new = new.next
                
        if(carry):
            new.next = ListNode(carry)
        
        return head.next
            
                
                
                
        