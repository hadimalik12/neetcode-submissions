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
        if not head:
            return None
        
        hm = {}
        curr = head

        while curr:
            new = Node(curr.val)
            hm[curr] = new
            curr = curr.next
        
        curr2 = head
        while curr2:
            copy = hm[curr2]

            copy_next = None
            if curr2.next:
                copy_next = hm[curr2.next]
            
            copy_rand = None
            if curr2.random:
                copy_rand = hm[curr2.random]
            
            copy.next = copy_next
            copy.random = copy_rand
            curr2 = curr2.next
        
        return hm[head]

        
            


