# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 1

        def dfs(node, big):
            nonlocal count
            if not node:
                return
            if node.val >= big:
                if node.val > big:
                    big = node.val
                count += 1
            
            dfs(node.left, big)
            dfs(node.right, big)
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return count