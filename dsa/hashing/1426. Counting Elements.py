class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        seen = set(arr)
        for num in arr:
            if num + 1 in seen:
                ans += 1
        return ans