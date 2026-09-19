class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = ans = curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                ans = min(ans, right - left + 1) if ans else right - left + 1
                curr -= nums[left]
                left += 1
        return ans