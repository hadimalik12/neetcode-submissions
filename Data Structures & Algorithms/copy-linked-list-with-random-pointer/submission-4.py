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
        hm = {None: None}
        curr = head

        while curr:
            new = Node(curr.val)
            hm[curr] = new
            curr = curr.next
        
        curr2 = head
        while curr2:
            copy = hm[curr2]
            copy.next = hm[curr2.next]
            copy.random = hm[curr2.random]
            curr2 = curr2.next
        
        return hm[head]

        
            


