class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = {0}
        def dfs(node):
            for key in rooms[node]:
                if key not in seen:
                    seen.add(key)
                    dfs(key)
        dfs(0)
        return len(seen) == len(rooms)