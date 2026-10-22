# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        if length == 1:
            return None
        
        idx = length - n
        counter = 0
        curr2 = head

        while counter < idx-1:
            curr2 = curr2.next
            counter+=1
        
        if n == 1:
            curr2.next = None
        elif idx == 0:
            return head.next
        else:
            curr2.next = curr2.next.next
        
        return head

