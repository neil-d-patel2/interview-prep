# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        
        cur = head
        length = length // 2
        for _ in range(length):
            cur = cur.next
        
        l1 = head
        l2 = cur

        while l1.val != cur.val and l2:
            temp1 = l1.next
            l1.next = l2
            l1 = temp1
            temp2 = l2.next
            l2.next = temp1
            l2 = temp2



        

        
        


