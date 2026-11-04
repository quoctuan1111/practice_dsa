# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        def dfs(node, parent):
            if not node:
                return
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
            dfs(node.left, parent)
            dfs(node.right, parent)

        parent = {}
        dfs(root, parent)
        queue = deque([target])
        seen = {target}
        while queue and k > 0:
            curr_length = len(queue)
            for _ in range(curr_length):
                node = queue.popleft()
                for neighbor in [node.left, node.right, parent.get(node)]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            k -= 1
        return [node.val for node in queue]

