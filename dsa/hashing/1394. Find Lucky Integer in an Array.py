class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = defaultdict(int)
        for num in arr:
            c[num] += 1
        ans = -1
        for num, freq in c.items():
            if num == freq:
                ans = max(ans, num)
        return ans