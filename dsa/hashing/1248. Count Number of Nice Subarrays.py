class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1
        ans = curr = 0
        for num in nums:
            curr += num % 2
            ans += count[curr - k]
            count[curr] += 1
        return ans       