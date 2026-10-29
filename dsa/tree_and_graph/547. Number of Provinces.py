class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        seen = set()
        ans = 0
        def dfs(i):
            seen.add(i)
            for neigbor in graph[i]:
                if neigbor not in seen:
                    dfs(neigbor)

        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans