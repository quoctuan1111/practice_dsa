class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        max_freq = max(count.values())
        ans = 0
        for freq in count.values():
            if freq == max_freq:
                ans += freq
        return ans
