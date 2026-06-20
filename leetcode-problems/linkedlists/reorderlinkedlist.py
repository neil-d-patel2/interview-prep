# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == null:
            return []

        cur = head 
        count = 1

        while cur.next:
            cur = cur.next 
            count += 1
        
        cur = head
        for i in range(count // 2):
            cur = cur.next

        # head is the beginning of the list 
        # cur is the middle of the list, need to reverse it 

        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # now, cur is the head of the reverse linked list
        out = []
        while head and cur:
            out.append(head.val)
            out.append(cur.val)
            continue
        
        
        


