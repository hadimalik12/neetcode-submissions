# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, subroot):
            if not root and not subroot:
                return True
            elif not root or not subroot:
                return False
            elif root.val != subroot.val:
                return False
            else:
                return check(root.left, subroot.left) and check(root.right, subroot.right)

        if not root:
            return False
        
        if check(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)