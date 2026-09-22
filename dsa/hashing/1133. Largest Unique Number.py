class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        largest = -1

        for num, frequency in count.items():
            if frequency == 1:
                largest = max(largest, num)

        return largest