# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """ 
        self.ans = root.val
        def dfs(node):
            if node is None:
                return
            if node.val == target:
                self.ans = node.val
                return 
            if abs(node.val - target) < abs(self.ans -target) or (abs(node.val - target) == abs(self.ans - target) and node.val < self.ans):
                self.ans = node.val
            if target < node.val:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)
        dfs(root)
        return self.ans