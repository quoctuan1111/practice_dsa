class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def check(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total <= threshold
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left