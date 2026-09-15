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
        cache = {}
        curr = head
        while curr:
            cache[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            cache[curr].next = cache.get(curr.next)
            cache[curr].random = cache.get(curr.random)
            curr = curr.next
        
        return cache.get(head)