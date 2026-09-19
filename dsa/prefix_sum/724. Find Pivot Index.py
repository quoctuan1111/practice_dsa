class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        total = prefix[-1]
        for i in range(len(nums)):
            left = prefix[i]
            right = total - left - nums[i]
            if left == right:
                return i 
        return -1