# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        node = dummy

        curr1 = l1
        curr2 = l2
        
        carry = 0

        while curr1 or curr2:
            if curr1 and curr2:
                tot = curr1.val + curr2.val + carry
                carry = tot // 10
                val = tot % 10
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1:
                tot = curr1.val + carry
                carry = tot // 10
                val = tot % 10
                curr1 = curr1.next
            else:
                tot = curr2.val + carry
                carry = tot // 10
                val = tot % 10
                curr2 = curr2.next
            
            new_node = ListNode(val)
            node.next = new_node
            node = node.next

        if carry != 0:
            new_node = ListNode(carry)
            node.next = new_node

        return dummy.next



