# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([(root, 0)])

        while queue:
            current, idx = queue.popleft()
            if idx <= len(result) - 1:
                result[idx].append(current.val)
            else:
                result.append([current.val])

            if current.left: queue.append((current.left, idx+1))
            if current.right: queue.append((current.right, idx+1))
        
        return result