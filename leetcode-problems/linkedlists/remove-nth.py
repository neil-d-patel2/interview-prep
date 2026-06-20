# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        cur = head
        count = 1

        while cur.next:
            cur = cur.next
            count += 1
        
        cur = head
        index = count - n - 1 
        
        if index == -1:
            head = head.next
            return head

        for i in range(index):
            cur = cur.next

        cur.next = cur.next.next

        return head






