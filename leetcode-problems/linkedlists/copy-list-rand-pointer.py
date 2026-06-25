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
                
          
        if head == None:
            return None

        cur = head
        myList = Node(0)
        out = myList
        h = { }

        while cur:
            myList.val = cur.val
            myList.next = ListNode(None)
            h[cur] = myList

            myList = myList.next
            cur = cur.next
        
        print(h)
        # Now, out is the head of our copy

        cur = head
        listCopy = out

        while cur:
            listCopy.random = h[cur.random]
            listCopy = listCopy.next
            cur = cur.next

     
        return out 



