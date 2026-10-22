# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxsofar):
            if node is None:
                return 0
            is_good = node.val >= maxsofar
            count = 1 if is_good else 0
            maxsofar = max(maxsofar, node.val)
            left = dfs(node.left, maxsofar)
            right = dfs(node.right, maxsofar)
            return count + left + right
        return dfs(root, root.val)
