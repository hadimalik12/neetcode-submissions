# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                new.next = curr1
                curr1 = curr1.next
            else:
                new.next = curr2
                curr2 = curr2.next
            new = new.next
        
        while curr1:
            new.next = curr1
            new = new.next
            curr1 = curr1.next
        
        while curr2:
            new.next = curr2
            new = new.next
            curr2 = curr2.next
        
        return dummy.next
        
        
        