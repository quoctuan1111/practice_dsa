class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        seen = set(nums)
        for num in range(0, n + 1):
            if num not in seen:
                return num
    