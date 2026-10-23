# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0
        def dfs(node, min_val, max_val):
            if node is None:
                return
            diff = max(abs(node.val - min_val), abs(node.val - max_val))
            self.ans = max (self.ans, diff)
            new_min = min(min_val, node.val)
            new_max = max(max_val, node.val)
            dfs(node.left, new_min, new_max)
            dfs(node.right, new_min, new_max)
        dfs(root, root.val, root.val)
        return self.ans

            
            