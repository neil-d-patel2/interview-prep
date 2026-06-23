#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        out = ListNode()
        value, rem = 0,0

        while l1 and l2:
            value = l1.val + l2.val + rem
            # if we do have a remainder
            if value > 10:
                append = value // 10 
                rem = value - (append * 10)
                out.val = append
                out.next = ListNode()
            else:
                rem = 0
                out.val = value
                out.next = ListNode()
                
            l1 = l1.next
            l2 = l2.next
    
        if rem != 0:     
            out.next.val = rem

        return out 



