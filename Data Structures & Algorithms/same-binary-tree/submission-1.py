# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(first, second):
            if not first and not second:
                return True
            elif not first or not second:
                return False
            elif first.val != second.val:
                return False
            else:
                return check(first.left, second.left) and check(first.right, second.right)
                
        
        return check(p, q)