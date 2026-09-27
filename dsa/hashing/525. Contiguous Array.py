class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        balance = 0
        first_seen = {0: -1}
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1
            if balance in first_seen:
                ans = max(ans, i - first_seen[balance])
            else:
                first_seen[balance] = i
        return ans